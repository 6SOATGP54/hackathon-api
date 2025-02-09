from vapi import app
from vapi import utils
from flask import request
import datetime
import ffmpeg
from flask import send_file
import shutil
import os
import logging
import awsgi

@app.route('/', methods=['GET', 'POST'])
def running():
    return 'Server is running'

@app.route('/download/zip', methods=['POST'])
def download():
    logging.info('Received request...')
    if 'file' not in request.files:
        logging.error('file not found')
        return 'Arquivo não enviado'
    
    file = request.files['file']
    logging.info(f'file: {file}')
    
    base_dir = os.path.join(app.config['STORAGE_FOLDER'], datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    video_file_dir = os.path.join(base_dir, 'video')
    imgs_files_dir = os.path.join(base_dir, 'imgs')
    zip_files_dir = os.path.join(base_dir, 'zip')

    video_file = os.path.join(video_file_dir, 'vimg-video.mp4')
    imgs_files = os.path.join(imgs_files_dir, 'vimg-%d.jpeg')
    zip_files = os.path.join(zip_files_dir, 'vimgs')
    zip_extension = 'zip'

    logging.info('Preparing processing dirs...')
    utils.make_storage_dir(base_dir, video_file_dir, imgs_files_dir, zip_files_dir)

    logging.debug('*******************Dirs**********************')
    logging.debug(base_dir)
    logging.debug(video_file_dir)
    logging.debug(imgs_files_dir)
    logging.debug(zip_files_dir)
    logging.debug('**********************files**********************')
    logging.debug(base_dir)
    logging.debug(video_file)
    logging.debug(imgs_files)
    logging.debug(zip_files)
 
    logging.info('Saving file...')
    file.save(video_file)
    file.close()
    logging.info('File saved')

    logging.info('Extracting images from video...')
    (
	ffmpeg.input(video_file)
	    .output(imgs_files)
	    .run()
    )
    logging.info('Extraction OK')

    logging.info('Zipping...')
    shutil.make_archive(zip_files, zip_extension, imgs_files_dir)
    logging.info('ZIP process is done')
    return send_file(f'{zip_files}.{zip_extension}', as_attachment=True)

def lambda_handler(event, context):
    print("Flask app started")
    return awsgi.response(app, event, context)

@app.route('/aws/post/test', methods=['POST'])
def aws_post():
    body = request.data
    print(body)
    return f'Received: {body}'
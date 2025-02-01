from vapi import app
from vapi import utils
from flask import request
import datetime
import ffmpeg
from flask import send_file
import shutil
import os

@app.route('/')
def running():
    return 'Server is running'

@app.route('/download/zip', methods=['POST'])
def download():
    if 'file' not in request.files:
        return 'Arquivo não enviado'
    
    file = request.files['file']
    print(file)
    
    base_dir = os.path.join(app.config['STORAGE_FOLDER'], datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    video_file_dir = os.path.join(base_dir, 'video')
    imgs_files_dir = os.path.join(base_dir, 'imgs')
    zip_files_dir = os.path.join(base_dir, 'zip')

    video_file = os.path.join(video_file_dir, 'vimg-video.mp4')
    imgs_files = os.path.join(imgs_files_dir, 'vimg-%d.jpeg')
    zip_files = os.path.join(zip_files_dir, 'vimgs')
    zip_extension = 'zip'

    utils.make_storage_dir(base_dir, video_file_dir, imgs_files_dir, zip_files_dir)

    print('*******************Dirs**********************')
    print(base_dir)
    print(video_file_dir)
    print(imgs_files_dir)
    print(zip_files_dir)
    print('**********************files**********************')
    print(base_dir)
    print(video_file)
    print(imgs_files)
    print(zip_files)
 
    file.save(video_file)
    file.close()

    (
	ffmpeg.input(video_file)
	    .output(imgs_files)
	    .run()
    )
    shutil.make_archive(zip_files, zip_extension, imgs_files_dir)
    return send_file(f'{zip_files}.{zip_extension}', as_attachment=True)
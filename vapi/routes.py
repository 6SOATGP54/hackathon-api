from vapi import app
from flask import request
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
    filename = os.path.join('/tmp', 'api', 'video', 'vimg-video.mp4')
    output = os.path.join('/tmp', 'api', 'imgs', 'vimg-%d.png')
    file.save(filename)
    file.close()

    (
	ffmpeg.input(filename)
	    .output(output)
	    .run()
    )
    shutil.make_archive('/tmp/api/compactado', 'zip', '/tmp/api/imgs')
    return send_file('/tmp/api/compactado.zip', as_attachment=True)
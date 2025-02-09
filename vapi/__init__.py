from flask import Flask
from vapi import utils
import os
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
app = Flask(__name__)
app.config['STORAGE_FOLDER'] = os.path.join('/tmp', 'api')

from vapi import routes
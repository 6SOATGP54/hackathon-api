from flask import Flask
from vapi import utils
import os

app = Flask(__name__)
app.config['STORAGE_FOLDER'] = os.path.join('/tmp', 'api')

from vapi import routes
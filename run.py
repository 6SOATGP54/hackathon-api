#!/usr/bin/env python3
from vapi import app
from vapi import utils

if __name__ == '__main__':
    utils.make_storage_dir(app.config['STORAGE_FOLDER'])
    app.run(host='0.0.0.0', port=5001, debug=True)
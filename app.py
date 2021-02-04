#! /home/xuchen/flask_downloader/venv/bin/python

from flask import Flask, send_from_directory
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

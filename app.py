#! /home/ubuntu/flask_downloader/venv/bin/python

import os

from flask import Flask, send_from_directory, render_template, request

from utils.file_classifier import classify

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/home')
@app.route('/')
def index():
   return render_template('home.html')

@app.route("/list_files")
def list_files():
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    _type = request.args.get("type")
    if _type == "all":
        files = {"files": os.listdir(uploads)}
    elif _type in ['backing', 'tabs', 'preset']:
        files = {"files": classify(uploads)[_type]}
    else:
        files = classify(uploads)
    return render_template('list_files.html', files=files)

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=1, port=80)

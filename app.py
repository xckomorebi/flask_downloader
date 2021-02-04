#! /home/ubuntu/flask_downloader/venv/bin/python


from flask import Flask, send_from_directory, render_template, url_for
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/home')
@app.route('/about')
@app.route('/')
def index():
   return render_template('home.html')

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

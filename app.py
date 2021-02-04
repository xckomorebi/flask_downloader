#! /home/ubuntu/flask_downloader/venv/bin/python


from flask import Flask, send_from_directory
import os
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
   return """<html>
    <title>xc简陋的主页</title>
    <body>
        <h1>小机灵鬼们你们好</h1>
        <h1>测试海外服务器需不需要备案</h1>
        <body>别问为啥这么简陋，问就是懒</body>
    </body>
</html>"""

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=uploads, filename=filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

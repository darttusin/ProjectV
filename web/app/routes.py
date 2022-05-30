from flask import render_template, request, flash, redirect, url_for, Flask
from app import app
import os
from werkzeug.utils import secure_filename
import requests
import time

name = "Unknown User"


@app.route ( '/', methods=['GET', 'POST'] )
def home():
    if request.method == 'POST':

        file = request.files['file']
        if file.filename[file.filename.find('.') + 1:len(file.filename)] != 'mp4':
            return render_template('error.html', title='Home')
        if file.filename == '':
            return redirect(request.url)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'hype.mp4'))
        time.sleep(10)
        try:
            requests.get('http://tracker-container:8081/start/',timeout=0.0000000001)
        except requests.exceptions.ReadTimeout: 
            pass
        return redirect(url_for('index'))
    return render_template ( 'home.html', title='Home')

@app.route ( '/index', methods=['GET', 'POST'] )
def index():
    return render_template ( 'index.html', title='Stream')
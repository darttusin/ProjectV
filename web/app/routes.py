from flask import render_template, request, flash, redirect, url_for, Flask
from app import app
import os
from werkzeug.utils import secure_filename


name = "Unknown User"


@app.route ( '/', methods=['GET', 'POST'] )
def home():
    if request.method == 'POST':

        file = request.files['file']
        if file.filename[file.filename.find('.') + 1:len(file.filename)] != 'mp4':
            return render_template('#', title='#')
        if file.filename == '':
            return redirect(request.url)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'hype.mp4'))
        return redirect(url_for('index'))
    return render_template ( 'home.html', title='Home')

@app.route ( '/index', methods=['GET', 'POST'] )
def index():
    global name
    username = request.form.get ( "username" )
    if username == None:
        user = {'username': name}
    else:
        user = {'username': username}
        name = username
    return render_template ( 'index.html', title='Stream', user=user )

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'hype.mp4'))
        return redirect(url_for('index'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Загрузите файл с расширением mp4 </h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
from flask import render_template, request, flash, redirect
from app import app

name = "Unknown User"


@app.route ( '/', methods=['GET', 'POST'] )
def home():
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

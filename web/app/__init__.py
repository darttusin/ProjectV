from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
UPLOAD_FOLDER = '../tracker/data/video'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes

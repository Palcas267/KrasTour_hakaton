from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = '123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
app.config['UPLOAD_FOLDER'] = 'static/images/'

admin_pass = 'error123'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'authorization'

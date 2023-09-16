from models import *
from config import db, app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.app_context().push()
db.create_all()

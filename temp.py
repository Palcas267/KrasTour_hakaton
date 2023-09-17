from config import app
from models import *
app.app_context().push()
db.create_all()

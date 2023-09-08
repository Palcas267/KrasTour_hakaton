from flask_login import UserMixin, current_user
from dataclasses import dataclass
from config import db

# Пользователи
@dataclass
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

# Товары (путевки)
@dataclass
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_track = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)

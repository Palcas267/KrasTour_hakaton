from flask_login import UserMixin, current_user
from dataclasses import dataclass
from config import db


# Пользователи
class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)


# Товары (путевки)
class Item(db.Model):
    __tablename__ = 'Item'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_track = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, default=True)

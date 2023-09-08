from flask_login import UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask import render_template, request, redirect, session
from config import db, login_manager, app, admin_pass
from models import User, Item
import os


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/register')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/admin')
def admin():
    if not session['admin_mode']:
        session['admin_mode'] = False
    return render_template('admin.html')


@app.route('/register')
def redister():
    return render_template('register.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


if __name__ == "__main__":
    app.run(debug=True)

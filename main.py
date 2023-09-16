from flask_login import UserMixin, current_user, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask import render_template, request, redirect, session
from config import db, login_manager, app, admin_pass
from models import *
import os


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/register')


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        try:
            email = request.form['email']
            user_name_filter = User.query.filter(User.email == email).one()
            user = User.query.get(user_name_filter.id)
            login_user(user, remember=True)
            return redirect('/profile')
        except:
            message = 'Нет аккаунтов с таким Email'
            return render_template('signing-in.html', message=message)
    else:
        return render_template('signing-in.html')


@app.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', )
    else:
        redirect('/register')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin')
def admin():
    if not session['admin_mode']:
        session['admin_mode'] = False
    return render_template('admin.html')


@app.route('/register', methods=['POST', 'GET'])
def redister():
    if request.method == 'POST':
        nickname = request.form['nickname']
        email = request.form['email']
        user_to_add = User(username=nickname, email=email)
        try:
            db.session.add(user_to_add)
            db.session.commit()
            login_user(user_to_add, remember=True)
            return redirect('/')
        except:
            message = 'Укажите другую почту или имя пользователя'
            return render_template('register.html', message=message)
    else:
        return render_template('register.html')


@app.route('/catalog')
def catalog():
    return render_template('catalog.html')


if __name__ == "__main__":
    app.run(debug=True, port=8080)

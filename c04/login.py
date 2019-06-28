import bcrypt as bcrypt
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for, session

from c05.userdb_utils import *

login_app = Blueprint('login_app',__name__)
app = login_app


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('w1.html')
    else:
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        if not username or not password:
            logging.error('Can not login.Username or password is empty.')
            flash(message='ユーザー名またはパスワードが入力されていません',category='Error')
            return redirect(url_for('login_app.login'))
        if len(username) > 255 or len(password) > 255:
            logging.error('Can not login.Username or password is longer than 255 characters.')
            flash(message='ユーザー名またはパスワードが256文字以上です',category='Error')
            return redirect(url_for('login_app.login'))

        user_info = fetch_user_info(username)
        if not user_info:
            logging.error("Can not login.Can not fetch user info.")
            flash(message='ユーザー名が間違っています',category='Error')
            return  redirect(url_for('login_app.login'))
        if bcrypt.hashpw(password,user_info[1].encode('utf-8')) == user_info[1].encode('utf-8'):
            session['username'] = user_info[0]
            session['permission'] = user_info[2]
            return  redirect(url_for('home'))
        else:
            logging.error('User and password not match.')
            flash(message='ユーザー名とパスワードが一致しません',category='Error')
            return  redirect(url_for('login_app.login'))





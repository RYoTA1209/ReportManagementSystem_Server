import bcrypt as bcrypt
from flask import Flask, render_template, Blueprint, request, flash, redirect, url_for, session
import logging

from c05.userdb_utils import *

register_app = Blueprint('register_app', __name__)
app = register_app

auth_code = "NMXGfD0hgon3nD717qoW4DfwP26I0u7I"


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'GET':
        return  render_template('w2.html')
    else:
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())
        permission = int(request.form['permission'])
        print(username,password,permission,sep=',')
        if not username or not password:
            logging.error('Cant create new account.Username or password is empty.')
            flash(message='ユーザー名かパスワードが入力されていません', category='Error')
            return  redirect(url_for('register_app.register'))

        if len(username) > 255 or len(password) > 255:
            logging.error('Cant create new account.Username or password is longer than 255 characters.')
            flash(message='ユーザー名またはパスワードが256文字以上です',category='Error')
            return redirect(url_for('register_app.register'))

        if permission == 1:
            input_code = request.form['code']
            if not input_code:
                logging.error('Cant create new account.code is empty.')
                flash(message='認証コードが入力されていません', category='Error')
                return redirect(url_for('register_app.register'))
            elif input_code != auth_code:
                logging.error('Cant create new account.Input code is not match.')
                flash(message='認証コードが違います', category='Error')
                return redirect(url_for('register_app.register'))
            else:
                logging.info('Authorization passed.')

        if is_already_exits(username):
            logging.error('Cant create new account.User already exist.')
            flash(message='ユーザー名が使用されています。別のユーザー名を入力してください',category='Error')
            return redirect(url_for('register_app.register'))
        userid = new_user(username,hash_pass,permission)
        if userid < 0:
            logging.error('Cant create new account.')
            flash(message='内部エラーが発生しました。時間をおいてもう一度試してください.',category='Error')
            return  redirect(url_for('register_app.register'))

        logging.info('New User Created.')
        session['username'] = username
        session['permission'] = permission
        session['userid'] = userid
        return  redirect(url_for('home'))

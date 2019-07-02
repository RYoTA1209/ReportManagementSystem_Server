#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint

# レポート管理部？
from c06.read_user_list import read_user_list  # 仮（生徒のユーザIDのリストをくれる）

order_user_list_app = Blueprint('order_user_list_app', __name__)
app = order_user_list_app


# ユーザーIDのリストの読み込みをレポート管理部に依頼する関数
@app.route('/user_list', methods=['GET', 'POST'])
def order_user_list():

    # user_id = session["username"]
    # report_list = read_user_list(user_id)

    user_list = read_user_list()

    # ユーザーIDのリストのテキストを返す
    return render_template("w18.html", u_list=user_list)  # w18.htmlは仮（ユーザーリストを表示させる）

#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint
from flask import request
import logging


# レポート管理部
from c06.delete_report_from_db_and_server import delete_report_from_db_and_server

order_delete_report_app = Blueprint('order_delete_report_app', __name__)
app = order_delete_report_app



# レポートの削除依頼をレポート管理部に依頼する関数
@app.route('/sakujo', methods=['GET', 'POST'])
def order_delete_report():

    # user_idが見つからなかったらエラーを返す
    # if 'user_id' not in request.form:
    #     logging.error("order_report_file: user_idをフォームから読み込めませんでした。")

    # assignment_idが見つからなかったらエラーを返す
    if 'assignment_id' not in request.form:
        logging.error("order_report_file: assignment_idをフォームから読み込めませんでした。")

    # フォームから受け取ったIDを格納
    # user_id = request.form['user_id']
    user_id = session["username"]

    # フォームから受け取った課題情報を格納
    assignment_id = request.form['assignment_id']

    # レポート管理部へID、課題情報を渡して論理値を得る
    success = delete_report_from_db_and_server(user_id, assignment_id)

    # 論理値の文字列を返す
    return render_template("w5.html")
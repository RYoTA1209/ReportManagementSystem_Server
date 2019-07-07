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

    # assignment_idが見つからなかったらエラーを返す
    if 'assignment_id' not in request.form:
        logging.error("order_delete_report: assignment_idをフォームから読み込めませんでした。")

    # 生徒からの閲覧か、指導者からW18空の閲覧かによってuser_idの分岐
    if session["permission"] == 0:

        # 生徒の場合はセッションから
        user_id = session["userid"]

    else:

        # user_idが見つからなかったらエラーを返す（指導者のみ）
        if 'user_id' not in request.form:
            logging.error("order_report_file: user_idをフォームから読み込めませんでした。")

        # 指導者の場合はフォームから
        user_id = request.form['user_id']  # w18にはuser_idをformに

    # フォームから受け取った課題番号を格納
    assignment_id = request.form['assignment_id']

    # レポート管理部へID、課題番号を渡して論理値を得る
    success = delete_report_from_db_and_server(user_id, assignment_id)

    # 理論値で例外処理
    if success != True:
        logging.error("order_delete_report: レポート削除に例外が発生しました。")

    # W5に遷移
    return render_template("w5.html")

#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint
from flask import request
import logging

# レポート管理部
# from c03.c06.write_feedback import write_feedback
from c06.write_feedback import write_feedback

order_store_feedback_app = Blueprint('order_store_feedback_app', __name__)
app = order_store_feedback_app


# フィードバックの書き込みをレポート管理部に依頼する関数
@app.route('/feedback', methods=['GET', 'POST'])
def order_store_feedback():

    # user_idが見つからなかったらエラーを返す
    if 'user_id' not in request.form:
        logging.error("order_store_feedback: user_idをフォームから読み込めませんでした。")

    # assignment_idが見つからなかったらエラーを返す
    if 'assignment_id' not in request.form:
        logging.error("order_store_feedback: assignment_idをフォームから読み込めませんでした。")

    # assignment_idが見つからなかったらエラーを返す
    if 'feedback_text' not in request.form:
        logging.error("order_store_feedback: feedback_textをフォームから読み込めませんでした。")

    # フォームから受け取ったIDを格納
    user_id = request.form['user_id']

    # フォームから受け取った課題番号を格納
    assignment_id = request.form['assignment_id']

    # フォームから受け取ったフィードバックの内容を格納
    feedback_text = request.form['feedback_text']

    # レポート管理部へID、課題番号、フィードバックを渡して論理値を得る
    success = write_feedback(user_id, assignment_id, feedback_text)

    # 理論値で例外処理
    if success != True:
        logging.error("order_store_feedback: レポート削除に例外が発生しました。")

    # W5に画面遷移
    return render_template("w5.html")

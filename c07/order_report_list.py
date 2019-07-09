#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint
from flask import request
import logging

# レポート管理部
# from c06.record_report_to_db import read_report_info
from c06.read_report_info import read_report_info

order_report_list_app = Blueprint('order_report_list_app', __name__)
app = order_report_list_app


# レポートリストの読み込みをレポート管理部に依頼する関数
@app.route('/list', methods=['GET', 'POST'])
def order_report_list():

    # 生徒からの閲覧か、指導者からの閲覧かによってuser_idの分岐
    if session["permission"] == 0:
        # 生徒の場合はセッションから
        user_id = session["userid"]

    else:
        # user_idが見つからなかったらエラーを返す（指導者のみ）
        if 'user_id' not in request.form:
            logging.error("order_report_list: user_idをフォームから読み込めませんでした。")

        # 指導者の場合はフォームから
        user_id = request.form['user_id']

    # レポート管理部へIDを渡してレポートリストを得る
    report_list = read_report_info(user_id)

    # 辞書型配列に格納
    report_dict = {
        "report_list": report_list,
        "user_id": user_id
    }

    # レポートのパスのリストを一つのテキストにする
    # report_path_text = ""
    # for line in report_list:
    #     report_path_text += (line + ",")

    # W11に画面遷移
    return render_template("w11.html", r_list=report_dict)

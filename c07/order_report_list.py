#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint
from flask import request
# import logging

# レポート管理部
# from c06.record_report_to_db import read_report_info
from c06.read_report_info import read_report_info

order_report_list_app = Blueprint('order_report_lit_app', __name__)
app = order_report_list_app


# レポートリストの読み込みをレポート管理部に依頼する関数
@app.route('/list', methods=['GET', 'POST'])
def order_report_list():

    # user_idが見つからなかったらエラーを返す
    # if 'user_id' not in request.form:
    #     logging.error("order_report_list: user_idをフォームから読み込めませんでした。")

    #TODO:useridを追加したので修正してください

    # 生徒からの閲覧か、指導者からW18空の閲覧かによってuser_idの分岐
    if session["permission"] == 0:
        # フォームから受け取ったIDを格納
        # user_id = request.form['user_id']
        user_id = session["username"]
    else:
        user_id = request.form['user_id']  # w18にはuser_idをformに

    # レポート管理部へIDを渡してレポートリストを得る
    report_list = read_report_info(user_id)

    list = {
        "report_list": report_list,
        "user_id": user_id
    }

    # レポートのパスのリストを一つのテキストにする
    # report_path_text = ""
    # for line in report_list:
    #     report_path_text += (line + ",")

    # レポートのリストのテキストを返す
    return render_template("w11.html", r_list=list)


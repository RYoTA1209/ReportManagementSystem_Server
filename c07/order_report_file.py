#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, session, Blueprint
from flask import request
# from flask import jsonify
import logging

# レポート管理部
from c06.read_report_file_path import read_report_file_path
from c06.read_feedback import read_feedback

# 文字コードによるバグの修正
import chardet

order_report_file_app = Blueprint('order_report_file_app', __name__)
app = order_report_file_app


# レポートとフィードバックを得る関数
@app.route('/etsuran', methods=['GET', 'POST'])
def order_report_file():

    # assignment_idが見つからなかったらエラーを返す
    if 'assignment_id' not in request.form:
        logging.error("order_report_file: assignment_idをフォームから読み込めませんでした。")

    # 生徒からの閲覧か、指導者からの閲覧かによってuser_idの分岐
    if session["permission"] == 0:
        # 生徒の場合はセッションから
        user_id = session["userid"]

    else:
        # user_idが見つからなかったらエラーを返す（指導者のみ）
        if 'user_id' not in request.form:
            logging.error("order_report_file: user_idをフォームから読み込めませんでした。")

        # 指導者の場合はフォームから
        user_id = request.form['user_id']

    # フォームから受け取った課題番号を格納
    assignment_id = request.form['assignment_id']

    # 単体テスト例
    # # フォームから受け取ったIDを格納
    # user_id = "1"
    #
    # # フォームから受け取った課題番号を格納
    # assignment_id = "1"

    # レポート管理部へID、課題番号を渡してレポートファイルのパスを得る
    report_file_path = read_report_file_path(user_id, assignment_id)

    '''
    try:
        # レポートファイルを開く
        report_file = open(report_file_path, "r", encoding="utf-8")
    except PermissionError:
        logging.error("order_report_file: パーミッションエラー")
    except IOError:
        logging.error("order_report_file: 入出力エラー")
    '''

    report_file=None
    # レポートファイルを開く
    try:
        with open(report_file_path, "rb") as f:
            character_code = chardet.detect(f.read())['encoding']
        global report_file
        report_file = open(report_file_path, "r", encoding=character_code)

    # パーミッションエラー
    except PermissionError:
        logging.error("order_report_file: パーミッションエラー")

    # 入出力エラー
    except IOError:
        logging.error("order_report_file: 入出力エラー")

    # レポートファイルを読み込む
    if(report_file is not None):
        report_text_list = report_file.readlines()
    else:
        report_text_list = list()
    # logging.info("report_text_list"+report_text_list[0])

    # レポートのテキストのリストを一つのテキストにする
    # report_text = ""
    # for line in report_text_list:
    #     report_text += line

    # レポート管理部へID、課題番号を渡してフィードバックのテキストを得る
    feedback_text = read_feedback(user_id, assignment_id)

    # 辞書型配列に追加
    result_dict = {
        "report_text_list": report_text_list,
        "feedback_text": feedback_text,
        "assignment_id": assignment_id,
        "user_id": user_id
    }
    # print(report_text)
    # print(feedback_text)

    # jsonファイル風にする
    # jsonify_result = jsonify(result_dict)

    # W12に画面遷移
    return render_template("w12.html", r_dict=result_dict)

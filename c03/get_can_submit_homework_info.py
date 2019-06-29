from flask import request, jsonify, Blueprint, render_template, session
import logging
import json

get_can_submit_homework_info_app = Blueprint('get_can_submit_homework_info', __name__)
app = get_can_submit_homework_info_app


@app.route('/get_can_submit_homework_info', methods=['GET'])
def get_can_submit_homework_info():

    if request.method == 'GET':

        #TODO:username is in session['username']
        # get userID from request
        if 'username' in session:
            user_id = session['username']
            logging.debug("get user_id from session")
        else:
            logging.error("username is not in session")
            return render_template("w7.html")

        #TODO:c9m2とはなんですか？
        homework_list = c9m2(user_id)
        if homework_list is None:
            logging.error("failed get from c9m2")
            return render_template("w7.html")
        else:
            logging.info("getting from c9m2 is success")

        logging.info("success get_can_submit_homework_info")

        return render_template("w7.html", homework_list=homework_list)


# コンポーネント9(c9)にあるはずのモジュール2(m2)です
# テスト用のスタブとして作りました
# c9m2が完成次第消します
# user_idを用いて提出できる宿題の情報をDBから検索、結果をリストとして返すものと想定しています
def c9m2(user_id):
    homework_list = list()

    ele1 = dict()
    ele1['homework_id'] = "1"
    ele1['about'] = "サンプルその1"

    ele2 = dict()
    ele2['homework_id'] = "2"
    ele2['about'] = "サンプルその2"

    homework_list.append(ele1)
    homework_list.append(ele2)

    return homework_list

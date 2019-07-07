from flask import request, jsonify, Blueprint, render_template, session, abort
import logging
import json

get_can_submit_homework_info_app = Blueprint('get_can_submit_homework_info', __name__)
app = get_can_submit_homework_info_app


@app.route('/get_can_submit_homework_info', methods=['GET'])
def get_can_submit_homework_info():

    if request.method == 'GET':

        # get userID from request
        if 'username' in session:
            user_id = session['userid']
            logging.debug("get user_id from session")
        else:
            logging.error("username is not in session")
            abort(404)

        homework_list = ret_homework_list(user_id)
        if homework_list is None:
            logging.error("failed get from c9m2")
            abort(404)
        else:
            logging.info("getting from c9m2 is success")

        logging.info("success get_can_submit_homework_info")

        return render_template("w7.html", homework_list=homework_list)


# 提出できる課題をリストにして返す関数
def ret_homework_list(user_id):
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

# hrefで画面遷移ができなくなるやつへの対処
# hrefで直接htmlを参照させるのではなく、
# flaskでレンダリングさせる
@app.route('/render_window/<window_name>')
def get_templates(window_name):
    return render_template(window_name)

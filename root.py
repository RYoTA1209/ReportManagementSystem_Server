import os

from flask import Flask, redirect, url_for, render_template

from c03.get_can_submit_homework_info import get_can_submit_homework_info_app
from c03.receive_uploaded_file import receive_uploaded_file_app
from c07.order_report_file import order_report_file_app
from c07.order_delete_report import order_delete_report_app
from c07.order_store_feedback import order_store_feedback_app
from c07.order_report_list import order_report_list_app
from c04.login import login_app
from c04.register import register_app

# add
from c07.order_user_list import order_user_list_app
# from c03.config import c03_module

import logging

app = Flask(__name__)
app.debug = True

app.register_blueprint(get_can_submit_homework_info_app)
app.register_blueprint(receive_uploaded_file_app)
app.register_blueprint(order_delete_report_app)
app.register_blueprint(order_report_file_app)
app.register_blueprint(order_store_feedback_app)
app.register_blueprint(order_report_list_app)
app.register_blueprint(login_app)
app.register_blueprint(register_app)

# add
app.register_blueprint(order_user_list_app)

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return redirect(url_for('login_app.login'))

@app.route('/home')
def home():
    return  render_template('w5.html')



logging.basicConfig(
    level=logging.DEBUG,
    format='%(module)-18s %(funcName)-10s %(lineno)4s: %(message)s'
)

if __name__ == '__main__':
    logging.debug("run app")
    app.run(host="0.0.0.0", port=80, threaded=True)

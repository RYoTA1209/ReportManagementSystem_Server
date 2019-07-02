# c9m1
from .connect_homework_db import connect_report_db, close_db
import logging
import mysql.connector

insert_homework_to_db = (
    "INSERT INTO test_table "
    "( title, summary, deadLine, homeworkID, userID ) "
    "VALUES ( %s, %s, %s, %s)"
)


def register_homework_info(title, summary, dead_line, homework_id, user_id):

    cnx = connect_report_db()
    # check connecting to report_db is success
    if cnx is None:
        logging.error("failed get connector")
        return -1
    cursor = cnx.cursor()

    try:
        cursor = cnx.sursor()
        cursor.execute(register_homework_info, (title, summary, dead_line, homework_id, user_id))

    except mysql.connector.Error as err:
        logging.error("failed add homework_info to db")
        logging.error(err)
        close_db(cursor, cnx)
        return False

    cursor.close()
    cnx.close()
    logging.info("close connector")

    return True

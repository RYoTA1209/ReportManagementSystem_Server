# c9m2
from .connect_homework_db import connect_report_db, close_db
import logging
import mysql.connector

select_all_homework_info = (
    "SELECT * FROM test_table "
)


def select_all_homework():

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

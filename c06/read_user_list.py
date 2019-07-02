# 新たに作ったw18.htmlに遷移するときに使う
import mysql.connector
from .connect_report_db import connect_report_db, close_db
import logging

read_user_list_who_had_submitted = (
    "SELECT userID from test_table GROUP BY userID "
)


def read_user_list():

    cnx = connect_report_db()
    if cnx is None:
        logging.error("failed get connector")
        return list()

    try:
        cursor = cnx.cursor()
        cursor.execute(read_user_list_who_had_submitted)
        result = cursor.fetchall()
        logging.info("get user list from db is success")

        cursor.close()
        cnx.close()
        logging.info("close connector")
    except mysql.connector.Error as err:
        logging.error("failed get user list from db")
        logging.error(err)
        close_db(cursor, cnx)
        return list()
    print(result)

    for i in range(len(result)):
        result[i] = result[i][0]

    return result


if __name__ == '__main__':

    print(read_user_list)

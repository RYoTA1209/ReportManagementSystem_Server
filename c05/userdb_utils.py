import mysql
import mysql.connector as connector
from mysql.connector import errorcode

import  logging

config = {
    "user":"user_db_user",
    "password":"qazwsx",
    # "host":"localhost",
    "host":"172.21.33.67",
    "port":"3306",
    "database":"USERDB",
    "raise_on_warnings":True,
    "charset":"utf8"
}


def connect_db():
    try:
        cnx = connector.connect(**config)
    except connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.error("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            logging.error("Database does not exist")
        else:
            logging.error(e.msg)
        return  None
    else:
        return cnx


def close_db(cursor,cnx):
    cursor.close()
    cnx.close()


def new_user(username,hash_pass,permission):

    cnx = connect_db()
    if not cnx:
        logging.error("failed connect db")
        return False

    cnx.autocommit = False

    try:
        cur = cnx.cursor()
        if is_already_exits(username):
            logging.error("Could not create new account.Because User already exits.")
            return False
        cur.execute("INSERT INTO users VALUES (%s,%s,%s)",(username,hash_pass,permission))
    except mysql.connector.Error as e:
        logging.error("Could not create new account.Something error occurred.")
        logging.error(e.msg)
        return False

    cnx.commit()
    close_db(cur,cnx)

    logging.info("Connector closed.")
    logging.info("Created new Account.")
    return True


def fetch_user_info(username):

    cnx = connect_db()
    if not cnx:
        logging.error("Failed connect db.")
        return False

    cnx.autocommit = False

    try:
        cur = cnx.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        if not user:
            logging.error("User not found.")
            close_db(cur,cnx)
            return None
        close_db(cur,cnx)
        logging.info("User fetch successful.")
        return user
    except mysql.connector.Error as e:
        logging.error("Could not fetch account.Something error occurred.")
        logging.error(e.msg)
        return None


def is_already_exits(username):
    cnx = connect_db()
    if not cnx:
        logging.error("failed connect db")
        return False
    cnx.autocommit = False
    try:
        cur = cnx.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s",(username,))
        user = cur.fetchone()
        if user:
            logging.error("User already exist.")
            close_db(cur,cnx)
            return True
        close_db(cur,cnx)
        return False
    except mysql.connector.Error as e:
        logging.error(e.msg)
        cnx.close()
        return None

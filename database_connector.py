# database_connector.py
import mysql.connector
from mysql.connector import errorcode
import config

def connection():
    try:
        conn = mysql.connector.connect(
            host=config.mysql_host,
            user=config.mysql_user,
            password=config.mysql_password,
            database=config.mysql_database,
        )
        cursor = conn.cursor()
        cursor.execute("SET foreign_key_checks = 1;")
        return conn, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The specified database does not exist.")
        else:
            print(f"Error: {err}")
        raise

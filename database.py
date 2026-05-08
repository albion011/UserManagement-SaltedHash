import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",
        database="user_management"
    )

def init_db():
    conn = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password=""
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS user_management")

    conn.commit()
    conn.close()
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="silent_sky"
    )

def insert_journal(user_id, entry, emotion):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO journal (user_id, entry, emotion, timestamp) VALUES (%s, %s, %s, %s)",
        (user_id, entry, emotion, datetime.now())
    )
    conn.commit()
    conn.close()

def get_today_logs(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT entry FROM journal WHERE user_id=%s AND DATE(timestamp)=CURDATE()",
        (user_id,)
    )
    logs = cursor.fetchall()
    conn.close()
    return " ".join([log[0] for log in logs])

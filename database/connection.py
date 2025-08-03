# database/connection.py
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
    except Exception as e:
        print("❌ Gagal koneksi ke DB:", e)
        return None

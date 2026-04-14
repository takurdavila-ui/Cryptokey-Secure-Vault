# auth/register.py

from storage.db import get_connection
from auth.hash_utils import hash_password
import getpass


def register_user():
    conn = get_connection()
    cursor = conn.cursor()

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    password_hash = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        print("✅ User registered successfully!")

    except Exception as e:
        print("❌ Error:", e)
        print("⚠️ Username might already exist.")

    finally:
        conn.close()
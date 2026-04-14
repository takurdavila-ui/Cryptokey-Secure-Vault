# auth/login.py

from storage.db import get_connection
from auth.hash_utils import verify_password
import getpass
import random

MAX_ATTEMPTS = 3


def login_user():
    conn = get_connection()
    cursor = conn.cursor()

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        cursor.execute(
            "SELECT id, password_hash FROM users WHERE username = ?",
            (username,)
        )

        user = cursor.fetchone()

        if user:
            user_id, stored_hash = user

            if verify_password(stored_hash, password):
                print("✅ Password verified!")

                # OTP
                otp = str(random.randint(100000, 999999))
                print(f"📩 Your OTP is: {otp}")

                user_otp = input("Enter OTP: ")

                if user_otp == otp:
                    print("✅ Login successful with 2FA!")
                    conn.close()
                    return user_id
                else:
                    print("❌ Invalid OTP")

            else:
                print("❌ Incorrect password")

        else:
            print("❌ User not found")

        attempts += 1
        print(f"⚠️ Attempts left: {MAX_ATTEMPTS - attempts}")

    print("🚫 Too many failed attempts. Try again later.")
    conn.close()
    return None
# storage/vault.py

from storage.db import get_connection
from crypto.encrypt import encrypt_data, decrypt_data


# 🔐 Add Password
def add_password(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    site = input("Enter site (e.g., gmail): ")
    username = input("Enter site username: ")
    password = input("Enter password: ")

    encrypted_password = encrypt_data(password)

    cursor.execute(
        "INSERT INTO vault (user_id, site, username, password) VALUES (?, ?, ?, ?)",
        (user_id, site, username, encrypted_password)
    )

    conn.commit()
    conn.close()

    print("✅ Password saved securely!")


# 👁️ View Passwords
def view_passwords(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT site, username, password FROM vault WHERE user_id = ?",
        (user_id,)
    )

    records = cursor.fetchall()

    if not records:
        print("⚠️ No passwords stored.")
    else:
        print("\n🔐 Your Stored Passwords:")
        for site, username, encrypted_password in records:
            decrypted_password = decrypt_data(encrypted_password)
            print(f"Site: {site} | Username: {username} | Password: {decrypted_password}")

    conn.close()


# ❌ Delete Password
def delete_password(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, site, username FROM vault WHERE user_id = ?",
        (user_id,)
    )

    records = cursor.fetchall()

    if not records:
        print("⚠️ No passwords to delete.")
        conn.close()
        return

    print("\n🔐 Your Stored Passwords:")
    for record in records:
        print(f"ID: {record[0]} | Site: {record[1]} | Username: {record[2]}")

    try:
        delete_id = int(input("Enter ID to delete: "))

        cursor.execute(
            "DELETE FROM vault WHERE id = ? AND user_id = ?",
            (delete_id, user_id)
        )

        if cursor.rowcount == 0:
            print("❌ Invalid ID")
        else:
            conn.commit()
            print("✅ Password deleted successfully!")

    except:
        print("❌ Invalid input")

    finally:
        conn.close()


# 🔍 Search Password
def search_password(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    search_site = input("Enter site name to search: ")

    cursor.execute(
        "SELECT site, username, password FROM vault WHERE user_id = ? AND site LIKE ?",
        (user_id, f"%{search_site}%")
    )

    records = cursor.fetchall()

    if not records:
        print("❌ No matching records found.")
    else:
        print("\n🔍 Search Results:")
        for site, username, encrypted_password in records:
            decrypted_password = decrypt_data(encrypted_password)
            print(f"Site: {site} | Username: {username} | Password: {decrypted_password}")

    conn.close()
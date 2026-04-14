# main.py

from storage.db import create_tables
from auth.register import register_user
from auth.login import login_user
from storage.vault import add_password, view_passwords, delete_password, search_password
from utils.session import SessionManager
from utils.generator import generate_password, check_strength


# 🔐 User Vault Menu
def user_menu(user_id):
    session = SessionManager(timeout=30)

    while True:
        if not session.is_session_active():
            print("⏳ Session expired! Auto logout.")
            break

        print("\n==== VAULT MENU ====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Generate Password")
        print("4. Delete Password")
        print("5. Search Password")
        print("6. Logout")

        choice = input("Enter choice: ")

        session.update_activity()

        if choice == "1":
            add_password(user_id)

        elif choice == "2":
            view_passwords(user_id)

        elif choice == "3":
            pwd = generate_password()
            strength = check_strength(pwd)

            print(f"Generated Password: {pwd}")
            print(f"Strength: {strength}")

        elif choice == "4":
            delete_password(user_id)

        elif choice == "5":
            search_password(user_id)

        elif choice == "6":
            print("🔒 Logging out...")
            break

        else:
            print("❌ Invalid choice")


# 🏠 Main Menu
def main_menu():
    while True:
        print("\n==== CRYPTOKEY PASSWORD MANAGER ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            user_id = login_user()

            # 🔐 If login fails (attempt limit or wrong credentials)
            if user_id is None:
                print("⚠️ Login failed or blocked. Returning to main menu.")
                continue

            # ✅ Successful login
            print(f"🎉 Welcome User ID: {user_id}")
            user_menu(user_id)

        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice")


# ▶️ Start Program
if __name__ == "__main__":
    create_tables()
    main_menu()
    
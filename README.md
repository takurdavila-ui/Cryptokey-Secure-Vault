# Cryptokey-Secure-Vault
Secure Password Manager with AES Encryption, Argon2 Hashing, 2FA Authentication, and Brute-Force Protection
# 🔐 Cryptokey Secure Vault

A secure and advanced password manager built using Python, designed to protect user credentials using strong encryption and modern cybersecurity techniques.

---

## 🚀 Key Features

- 🔑 User Registration & Login System  
- 🔒 Secure Password Hashing using Argon2  
- 🔐 AES Encryption for protecting stored credentials  
- 📩 Two-Factor Authentication (OTP-based login)  
- 🚫 Login Attempt Limiter (prevents brute-force attacks)  
- 🗂️ Secure Password Vault  
  - Add Password  
  - View Passwords  
  - Delete Password  
  - Search Password  
- 🔄 Auto Logout after inactivity  
- 🔐 Strong Password Generator  
- 📊 Password Strength Checker  

---

## 🧠 Tech Stack

- **Python 3**
- **SQLite3** – Database
- **Argon2** – Password Hashing
- **PyCryptodome (AES)** – Encryption
- **Standard Python Libraries**

---

## 📁 Project Structure

cryptokey/
│
├── main.py
├── requirements.txt
│
├── auth/
│ ├── login.py
│ ├── register.py
│ └── hash_utils.py
│
├── crypto/
│ └── encrypt.py
│
├── storage/
│ ├── db.py
│ └── vault.py
│
├── utils/
│ ├── generator.py
│ └── session.py
│
├── data/
│ └── vault.db

---

## ▶️ How to Run

### 1. Clone the Repository
git clone https://github.com/your-username/cryptokey.git

cd cryptokey

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run Application
python main.py

---

## 🔐 Security Highlights

- **Argon2 Hashing** ensures passwords are securely stored
- **AES Encryption** protects all sensitive data
- **OTP-based 2FA** adds an extra authentication layer
- **Login Attempt Limiter** prevents brute-force attacks
- **Session Timeout** ensures automatic logout

---

## 📊 Project Highlights

- Combines **Cybersecurity + Cryptography + Real-world Application**
- Implements **secure authentication and encryption techniques**
- Designed using a **modular and scalable architecture**
- Includes **research-based approach (Post-Quantum Cryptography benchmarking)**

---

## 🔮 Future Enhancements

- Cloud-based encrypted storage
- GUI (React / Tkinter)
- Biometric authentication
- Browser extension integration

---

## 👩‍💻 Author

**Devisri Thakur**  
B.Tech CSE  
Shadan Women’s College of Engineering and Technology  

---

## ⭐ Note

This project is developed for educational purposes and demonstrates secure password management concepts.

---

⭐ If you found this project useful, give it a star!

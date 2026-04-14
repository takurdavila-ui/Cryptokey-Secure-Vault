# crypto/encrypt.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# AES key (in real apps, store securely)
SECRET_KEY = b'1234567890123456'  # 16 bytes key


def encrypt_data(data):
    """
    Encrypt plain text data
    """
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())

    encrypted = base64.b64encode(
        cipher.nonce + tag + ciphertext
    ).decode()

    return encrypted


def decrypt_data(encrypted_data):
    """
    Decrypt encrypted data
    """
    decoded = base64.b64decode(encrypted_data.encode())

    nonce = decoded[:16]
    tag = decoded[16:32]
    ciphertext = decoded[32:]

    cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
    decrypted = cipher.decrypt_and_verify(ciphertext, tag)

    return decrypted.decode()
# auth/hash_utils.py

from argon2 import PasswordHasher

# Create Argon2 object
ph = PasswordHasher()


def hash_password(password):
    """
    Hash the password securely
    """
    return ph.hash(password)


def verify_password(stored_hash, password):
    """
    Verify password with stored hash
    """
    try:
        return ph.verify(stored_hash, password)
    except:
        return False
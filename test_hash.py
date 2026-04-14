from auth.hash_utils import hash_password, verify_password

password = "mypassword123"

# Hash password
hashed = hash_password(password)
print("Hashed:", hashed)

# Verify correct password
print("Correct password:", verify_password(hashed, "mypassword123"))

# Verify wrong password
print("Wrong password:", verify_password(hashed, "wrongpass"))
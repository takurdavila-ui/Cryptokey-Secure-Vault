from crypto.encrypt import encrypt_data, decrypt_data

data = "mysecretpassword"

encrypted = encrypt_data(data)
print("Encrypted:", encrypted)

decrypted = decrypt_data(encrypted)
print("Decrypted:", decrypted)
# encryption_decryption.py
from cryptography.fernet import Fernet

def generate_key():
    """Генерация ключа для шифрования"""
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def encrypt_file(input_file, output_file, key):
    """Шифрование содержимого файла"""
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f"Файл '{input_file}' зашифрован и сохранен как '{output_file}'")

def decrypt_file(input_file, output_file, key):
    """Дешифрование содержимого файла"""
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)
    print(f"Файл '{input_file}' расшифрован и сохранен как '{output_file}'")

if __name__ == "__main__":
    # Генерация ключа
    key = generate_key()
    
    # Шифрование файла
    encrypt_file('secret.txt', 'secret_encrypted.txt', key)
    
    # Дешифрование файла
    decrypt_file('secret_encrypted.txt', 'secret_decrypted.txt', key)

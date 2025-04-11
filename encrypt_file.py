from cryptography.fernet import Fernet

def generate_key():
    """Генерация ключа для шифрования"""
    return Fernet.generate_key()

def encrypt_file(input_file, output_file, key):
    """Шифрование содержимого файла"""
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)
    print(f"Файл '{input_file}' зашифрован и сохранен как '{output_file}'")

if __name__ == "__main__":
    key = generate_key()
    print(f"Сгенерированный ключ: {key.decode()}")
    encrypt_file('secret.txt', 'secret_encrypted.txt', key)

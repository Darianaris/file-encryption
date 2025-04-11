1. Назначение программы
Программа предназначена для шифрования и дешифрования файлов с использованием библиотеки cryptography и алгоритма симметричного шифрования Fernet. Она обеспечивает безопасность данных за счет шифрования содержимого файлов.
2. Условия выполнения программы
Установленная библиотека cryptography. Установка производится через команду:
pip install cryptography
Наличие файла secret.txt в рабочей директории для шифрования и дешифрования.
3. Описание задачи
Задача программы заключается в следующем:
Сгенерировать ключ для шифрования.
Зашифровать содержимое входного файла и сохранить его в новый выходной файл.
Дешифровать содержимое зашифрованного файла и сохранить его в новый файл.
4. Алгоритм решения задачи
Сгенерировать ключ для шифрования с помощью функции generate_key.
Зашифровать файл secret.txt, используя сгенерированный ключ, и сохранить его как secret_encrypted.txt.
Дешифровать файл secret_encrypted.txt и сохранить его как secret_decrypted.txt.
5. Функционирование программы
Программа запускается из основного блока if __name__ == "__main__":, где происходит генерация ключа, шифрование и дешифрование файла.
6. Тексты сообщений оператору
"Сгенерированный ключ: {key}" — сообщение о создании ключа.
"Файл '{input_file}' зашифрован и сохранен как '{output_file}'" — сообщение об успешном шифровании.
"Файл '{input_file}' расшифрован и сохранен как '{output_file}'" — сообщение об успешном дешифровании.
7. Выходная информация
Создание файла с зашифрованным содержимым.
Создание файла с расшифрованным содержимым (для функции дешифрования).
Генерируемый ключ при каждом запуске программы.
8. Ошибки и аварийные ситуации
Ошибка при отсутствии входного файла (FileNotFoundError).
Ошибка при чтении или записи файлов (IOError).
Неверный формат ключа или повреждённые данные при дешифровании (InvalidToken).
9. Требования к документации
Документация должна содержать:
Описание установки и настройки необходимых библиотек.
Пошаговую инструкцию по запуску программы и описанию функций.
Инструкцию по работе с ошибками.
10. Дополнительные сведения
Программа поддерживает работу с любыми файлами и может применяться для защиты личных данных, а также в системах, где необходимо обеспечить конфиденциальность информации, хранящейся в файлах.


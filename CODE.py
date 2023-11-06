from Crypto.Cipher import DES

# запрос ключа у пользователя
key = input("Введите ключ: ")

# чтение сообщения из файла
with open('MES.txt', 'r', encoding='utf-8') as message_file:
    plaintext = message_file.read()

# шифрование сообщения
cipher = DES.new(key.encode(), DES.MODE_CFB, iv=None)
ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

# запись зашифрованного сообщения в файл
with open('RES.txt', 'wb') as output:
    output.write(ciphertext)

print("Исходное сообщение:", plaintext)
print("Ключ:", key)
print("Зашифрованное сообщение (бинарные данные):", ciphertext)
print("Зашифрованное сообщение (декодированное):", ciphertext.decode(encoding='utf-8', errors='ignore'))
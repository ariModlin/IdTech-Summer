def decimal_message_key():
    for i in range(len(unencrypted_message)):
        # converts the unencrypted message to decimal
        message_to_decimal = ord(unencrypted_message[i])
        decimal_message.append(message_to_decimal)
    for x in range(len(encryption_key)):
        # converts the key to decimal
        key_to_decimal = ord(encryption_key[x])
        decimal_key.append(key_to_decimal)
    return decimal_key, decimal_message
def message_key_encrypted(encrypted_message):
    decimal_message_key()
    for j in range(len(unencrypted_message)):
        new_numbers = decimal_message[j] ^ decimal_key [j]
        new_characters = chr(new_numbers)
        encrypted_message += new_characters
    return encrypted_message
def decrypting_message(decrypted_message):
    for p in range(len(e_message)):
        e_nums = ord(e_message[p])
        returning_numbers = e_nums ^ decimal_key[p]
        returning_chars = chr(returning_numbers)
        decrypted_message += returning_chars
    return decrypted_message
unencrypted_message = input("input message to encrypt: ")
encryption_key = input("input encryption key: ")
encrypted_message = ""
decrypted_message = ""
decimal_message = []
decimal_key = []


e_message = message_key_encrypted(encrypted_message)
d_message = decrypting_message(decrypted_message)
print(e_message)
print(d_message)


alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("input message you want to encrypt: ")
key = input("input key you want to encrypt the message with: ")
message_array = []
key_array = []
encrypted_numbers = []
decrypted_message = ""
def convert_message():
    for i in range(len(message)):
        # takes the message and converts the letters into numbers
        message_index = (alphabet.find(message[i]))
        message_array.append(message_index)
    return message_array


def convert_key():
    for j in range(len(key)):
        # takes the key and converts the letters into numbers
        key_index = (alphabet.find(key[j]))
        key_array.append(key_index)
    return key_array


def encrypt_message():
    encrypted_message = ""
    for x in range(len(message)):
        # adds each number letter from both the message array and the key array and mods 26 to get the new number
        new_num = (message_array[x] + key_array[x]) % 26
        # adds each new number to an encrypted numbers array
        encrypted_numbers.append(new_num)
        # converts each of the new numbers into its corresponding letter
        new_letters = alphabet[encrypted_numbers[x]]
        encrypted_message += new_letters
    print("encrypted message: " + encrypted_message)
    return encrypted_message


convert_message()
convert_key()
encrypt_message()
question = input("do you wish to see the message decrypted again? y/n ")
if question == "y":
    for a in range(len(encrypted_message)):
        decrypted_nums = encrypted_numbers[a] - key_array[a]
        if decrypted_nums < 0:
            decrypted_nums = 26 + decrypted_nums
        decrypted_letters = alphabet[decrypted_nums]
        decrypted_message += decrypted_letters
    print("decrypted message: " + decrypted_message)
else:
    print("goodbye")

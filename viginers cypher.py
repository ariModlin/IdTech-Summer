def amount_of_key_shift(key_shift):
    if key_shift == 0:
        new_alphabet = original_alphabet
    elif key_shift > 0:
        part_one = original_alphabet[:key_shift]
        part_two = original_alphabet[key_shift:]
        new_alphabet = part_two + part_one
    elif key_shift < 0:
        part_one = original_alphabet[:26+key_shift]
        part_two = original_alphabet[26+key_shift:]
        new_alphabet = part_two + part_one
    return new_alphabet


def create_array():
    for key_shift in range(26):
        new_alphabet = amount_of_key_shift(key_shift)
        cypher.append(new_alphabet)


original_alphabet = "abcdefghijklmnopqrstuvwxyz"
cypher = []
create_array()
message = input("input message you wish to encode: ")
encryption = input("input the encryption pattern: ")
message_array = []
encryption_array = []
print(cypher)
for i in range(len(message)):
    message_index = (original_alphabet.find(message[i]))
    message_array.append(message_index)
print(message_array)
for j in range(len(encryption)):
    encryption_index = (original_alphabet.find(encryption[j]))
    encryption_array.append(encryption_index)
print(encryption_array)
for i in range(len(message)):
    print(cypher[message_array[i]][encryption_array[i]])

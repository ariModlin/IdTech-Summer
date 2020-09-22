alphabet = "abcdefghijklmnopqrstuvwxyz"
key_shift = int(input("input shift: ")) % 26
part_one = ""
part_two = ""

if key_shift == 0:
    key = alphabet
elif key_shift > 0:
    part_one = alphabet[:key_shift]
    part_two = alphabet[key_shift:]
elif key_shift < 0:
    part_one = alphabet[:26+key_shift]
    part_two = alphabet[26+key_shift:]
key = part_two + part_one
print(key)
word = input("input word: ")
new_word = ""
letters = len(word)
for i in range(letters):
    letter_index = (alphabet.find(word[i]))
    if letter_index == -1:
        new_word += " "
    new_word += key[letter_index]
print(new_word)
# decrypt function
original_word = ""
for i in range(letters):
    letter_index1 = (key.find(new_word[i]))
    if letter_index1 == -1:
        original_word += " "
    original_word += alphabet[letter_index1]
print(original_word)

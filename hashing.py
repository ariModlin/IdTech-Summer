message = "Raymond"
total_hash = 0
array = [None]*256
for i in range(len(message)):
	num = ord(message[i])
	total_hash = 199 * total_hash + num
final_hash = total_hash % 199
array[final_hash] = message
for j, final_hash in enumerate(array):
	if array[j] != None:
		print(j, "->", final_hash)

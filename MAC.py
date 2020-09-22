# finds the MAC of a message using two different keys and a prime number
message = "blah blahs"
key1 = 15
key2 = 20
prime_num = 19

def find_mac():
	message_num = 0
	for i in range(len(message)):
	# takes each letter of the message and finds its ASCII counterpart
		num = ord(message[i])
	# adds each ASCII number to an integer message_num
		message_num += num
	# the mac of the message is equal to this equation
	m = ((key1 * message_num) + key2) % prime_num
	return m


mac = find_mac()
print(mac)
import math

prime_input = int(input("input number to see if its prime: "))
root_num = math.sqrt(prime_input)
if prime_input in range(0, 4):
	print("prime")
elif prime_input == 9:
	print("not prime number")
else:
	for numbers in range(2, math.floor(root_num)+1):
		if prime_input % numbers == 0:
			print("not prime number")
			break
		else:
			print("prime")
			break

# exchanges public keys using the Diffie–Hellman key exchange
bob = 3
public_mod = int(input("input the public modulus: "))
base = int(input("input the base number: "))


def public_key_exchange(alice):
	alice_one = (base ** alice) % public_mod
	bob_one = (base ** bob) % public_mod
	alice_key = (bob_one ** alice) % public_mod
	bob_key = (alice_one ** bob) % public_mod
	return alice_key


pkey = public_key_exchange(int(input("input alice's number: ")))
print(pkey)

# RSA Algorithm example for encryption and signatures


def gcd(a, b):
    # Find the greatest common divisor starting with a > b
    while b != 0:
        r = b
        b = a % b
        a = r
    return a


def lcm(a, b):
    num = a * b
    den = gcd(a, b)
    return num // den


def validate_public_key(key, carmichael):
    if key < 1:
        print("Key value too low")
    if key > carmichael:
        print("Key value too high")
    if gcd(key, carmichael) != 1:
        print("Key and λ(modulus) are not coprime")


def find_private_key(key, modulus):
    r = [modulus, key]
    q = [0, 0]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2] // r[index - 1]
        q.append(quotient)
        remainder = r[index - 2] - q[index] * r[index - 1]
        r.append(remainder)
        # Auxiliary number is the product of quotient and previous aux, plus 2nd previous aux
        aux = a[index - 2] - q[index] * a[index - 1]
        a.append(aux)
        index += 1
    inverse = a[len(a) - 2]
    if inverse < 0:
        inverse += modulus
    return inverse


def RSA_encrypt(message, key, modulus):
    cipherlist = []
    for c in message:
        number = ord(c)
        cipher = (number ** key) % modulus
        cipherlist.append(cipher)
    return cipherlist


def RSA_decrypt(cipher, key, modulus):
    message = ""
    for n in range(len(cipher)):
        number = (cipher[n] ** key) % modulus
        message += chr(number)
    return message


def new_hash(message):
    new_hash = 0
    for c in message:
        new_hash += ord(c)
        new_hash = new_hash % 256
    return new_hash


def write_signature(message, key, modulus):
    hashed_text = new_hash(message)
    signature = (hashed_text ** key) % modulus
    return signature


def check_signature(message, signature, key, modulus):
    hashed_text = new_hash(message)
    hash_check = signature ** key % modulus
    if hashed_text == hash_check:
        print("Signature is valid")
        return True
    else:
        print("Message is compromised")
        return False

      
# RSA Example constants. Items are marked as public or private
# Prime numbers and their Carmichael function λ(p*q) are kept as private items. Larger prime numbers are better!
primeP = 61
primeQ = 53
# The Carmichael function is technically based on the modulus below, but is equivalent to lcm(p - 1, q - 1). This is also private.
carmichael = lcm(primeP - 1, primeQ - 1)
# The modulus is used for both encryption and decryption, which means it makes a public appearance when encrypting!
modulus = primeP * primeQ
print(modulus)
# Choose the public key (for Alice). It has a few conditions but it helps to choose a prime number.
alice_public_key = 17
validate_public_key(alice_public_key, carmichael)
# The private key is derived from the chosen public key and is based on the private Carmichael value
alice_private_key = find_private_key(alice_public_key, carmichael)
#print(alice_private_key)
# Bob sends Alice an encrypted message using her public key
bob_plaintext = "Hello Alice"
bob_cipher = RSA_encrypt(bob_plaintext, alice_public_key, modulus)
print(bob_cipher)
# Alice receives Bob's message and decrypts it with her private key
bob_message = RSA_decrypt(bob_cipher, alice_private_key, modulus)
print(bob_message)

# Alice sends Bob a signed message using her private key
alice_plaintext = "Hello B"
alice_signature = write_signature(alice_plaintext, alice_private_key, modulus)
# Bob validates the hash with Alice's public key
alice_message = "Hello B."
hash_check = check_signature(alice_message, alice_signature, alice_public_key, modulus)
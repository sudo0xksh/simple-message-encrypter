import random
import string

print("=========================================")
print("Message Encrypter\n")

# characters set
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# key (shuffled characters)
key = chars.copy()
random.shuffle(key)

# ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"encrypted message: {cipher_text}")

# DECRYPT
decrypted_text = ""

for letter in cipher_text:
    index = key.index(letter)
    decrypted_text += chars[index]

print(f"original message: {decrypted_text}")

print("\n=========================================")
print("Developed by sudo_0xksh")
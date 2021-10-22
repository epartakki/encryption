## Resources: [C = (P+k)mod26], [C = (P-k)mod26]

# Create encryption function to encrypt a message using a key [C = (P+k)mod26]

def encrypt(message, key):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caeser = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) + key) % 26

            caeser = caeser+alphabet[letter_index]
    return caeser

print("~~~Welcome to the Caesar Cipher. Begin by encrypting a message!~~~\n~~~Note: everything will turn to uppercase~~~")
print("")
message = input("Enter message to encrypt: ")

# Makes everything uppercase to avoid lowercase cases
message = message.upper()

k = int(input("Enter Caesar shift number: "))
print("Encrypted Message: ", encrypt(message, k))



# Create decryption function to decrypt a ciphertext using a key[C = (P-k)mod26]

def decrypt(message, key):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    caeser = ""

    for letter in message:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - key) % 26

            caeser = caeser+alphabet[letter_index]
    return caeser

print("")
print("~~~Now, you can attempt to decrypt a message!~~~")
print("")
message = input("Enter message to decrypt: ")

# Makes everything uppercase to avoid lowercase cases
message = message.upper()

k = int(input("Enter Caesar shift number: "))
print("Decrypted Message: ", decrypt(message, k))

# ----------------- Variable field -----------------
text = ''
custom_key = ''

# ----------------- Functions -----------------
# Method for encrypting and decrypting a message based on the vigenere cipher
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

# ----------------- Interactable Functions -----------------
def Question():
    answer = input("Do you want to encrypt (E) or decrypt (D) a message?\n")
    if(answer.casefold() == "e"):
        message = input ("\nWhat message do you want to encrypt?\n")
        key = input ("What is the key for this message\n")
        print("\nEncrypted message: " + encrypt(message, key) + "\n")

    if(answer.casefold() == "d"):
        message = input ("\nWhat message do you want to decrypt?\n")
        key = input ("What is the key for this message\n")
        print("\nDecrypted message: " + decrypt(message, key) + "\n")
    
    # Run the question again after encrypting or decrypting
    Question()

# ----------------- Run Program -----------------
Question()
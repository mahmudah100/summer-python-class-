# The encrypted text (ciphertext) we want to decrypt
text = 'mrttaqrhknsw ih puggrur'

# The secret key used for the Vigenère cipher
custom_key = 'happycoding'


# General Vigenère cipher function (works for both encrypting and decrypting)
def vigenere(message, key, direction=1):
    key_index = 0                             # Keeps track of the current position in the key
    alphabet = 'abcdefghijklmnopqrstuvwxyz'   # The alphabet used for shifting
    final_message = ''                        # The result string (encrypted or decrypted)

    # Loop through each character in the message, converting to lowercase
    for char in message.lower():

        # If the character is NOT a letter (like spaces or punctuation),
        # just add it to the result without changes
        if not char.isalpha():
            final_message += char
        else:        
            # Pick the corresponding key character (wrap around using modulo if needed)
            key_char = key[key_index % len(key)]
            key_index += 1  # Move to the next key character for the next loop

            # Find the shift amount based on the key character's position in the alphabet
            offset = alphabet.index(key_char)

            # Find the index of the current message character in the alphabet
            index = alphabet.find(char)

            # Apply the Vigenère shift
            # direction = 1 → encryption, direction = -1 → decryption
            new_index = (index + offset * direction) % len(alphabet)

            # Append the new encrypted/decrypted character to the result
            final_message += alphabet[new_index]
    
    # Return the final encrypted or decrypted message
    return final_message


# Function to encrypt a message using the Vigenère cipher
def encrypt(message, key):
    return vigenere(message, key)


# Function to decrypt a message using the Vigenère cipher
def decrypt(message, key):
    return vigenere(message, key, -1)


# Print the original encrypted text
print(f'\nEncrypted text: {text}')

# Print the key being used
print(f'Key: {custom_key}')

# Decrypt the text using the key
decryption = decrypt(text, custom_key)

# Print the decrypted text (the original plain message)
print(f'\nDecrypted text: {decryption}\n')

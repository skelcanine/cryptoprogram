# XOR and Shifting Encoder/Decoder with Key Schedule

# Define a function to generate a key schedule from an initial key value
def generate_key_schedule(key, num_rounds):
    # Convert the key value to a bytes object 8 bit UTF-8
    key_bytes = key.to_bytes((key.bit_length() + 7) // 8, 'big')

    # Initialize an empty list to store the key schedule
    key_schedule = [key_bytes]

    # Generate a sequence of keys using a key schedule
    for i in range(num_rounds - 1):
        # Convert the current key bytes back to an integer
        key = int.from_bytes(key_bytes, 'big')

        # Perform a left shift by 3 bits on the key value
        key = (key << 3) | (key >> (32 - 3))

        # XOR the key value with the round numberxx
        key ^= i

        # Convert the updated key value to a bytes object
        key_bytes = key.to_bytes((key.bit_length() + 7) // 8, 'big')

        # Add the new key bytes to the key schedule
        key_schedule.append(key_bytes)

    # Return the final key schedule
    return key_schedule


# Define a function to encrypt plaintext using XOR and shifting operations with a key schedule
def xor_shift_encrypt(plaintext, key_schedule):
    # Initialize an empty string to store the ciphertext
    ciphertext = ""

    # Loop over each character in the plaintext
    for i, char in enumerate(plaintext):
        # Get the key bytes for the current round of encryption
        key_bytes = key_schedule[i % len(key_schedule)]

        # Shift the ASCII code of the current character by the current key byte
        shifted_char = chr((ord(char) + key_bytes[i % len(key_bytes)]) % 256)

        # XOR the shifted ASCII code with the next key byte in the sequence
        encrypted_char = chr(ord(shifted_char) ^ key_bytes[(i + 1) % len(key_bytes)])

        # Add the encrypted character to the ciphertext string
        ciphertext += encrypted_char

    # Return the encrypted ciphertext string
    return ciphertext


# Define a function to decrypt ciphertext using XOR and shifting operations with a key schedule
def xor_shift_decrypt(ciphertext, key_schedule):
    byte_array_of_cipher = []
    # Initialize an empty string to store the plaintext
    plaintext = ""

    # Loop over each character in the ciphertext
    for i, char in enumerate(ciphertext):
        # Get the key bytes for the current round of decryption
        key_bytes = key_schedule[i % len(key_schedule)]
        byte_array_of_cipher.append(ord(char).to_bytes((key.bit_length() + 7) // 8, 'big'))

        # XOR the ASCII code of the current character with the next key byte in the sequence
        decrypted_char = chr(ord(char) ^ key_bytes[(i + 1) % len(key_bytes)])

        # Shift the ASCII code of the decrypted character by the current key byte
        shifted_char = chr((ord(decrypted_char) - key_bytes[i % len(key_bytes)]) % 256)

        # Add the shifted character to the plaintext string
        plaintext += shifted_char

    # print("Cipher bytes:", byte_array_of_cipher)
    # Return the decrypted plaintext string
    return plaintext


# Example usage
plaintext = "Hello, World!"
key = 0xdeadbeefcafebabe
num_rounds = 17

# Generate a key schedule using the initial key value and number of rounds
key_schedule = generate_key_schedule(key, num_rounds)

# Encrypt the plaintext using the key schedule
encrypted_text = xor_shift_encrypt(plaintext, key_schedule)

# Print the encrypted ciphertext and key schedule
print("Encrypted text:", encrypted_text)
print("Key schedule:", key_schedule)


# Decrypt the ciphertext using the same key schedule
decrypted_text = xor_shift_decrypt(encrypted_text, key_schedule)

# Print the decrypted plaintext
print("Decrypted text:", decrypted_text)
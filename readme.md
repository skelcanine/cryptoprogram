# XOR and Shifting encryption, decryption algorithm with python

![Diagram of Algorithm](https://github.com/skelcanine/cryptoprogram/blob/master/pics/diagram.png?raw=true)

                
1.	The program starts by defining a function called `generate_key_schedule` that takes an initial key value and a number of rounds as input and returns a list of key values generated using a key schedule.

2.	The `generate_key_schedule` function first converts the initial key value to a bytes object using the `to_bytes` method.

3.	It then initializes an empty list to store the key schedule.

4.	The function then generates a sequence of key values using a key schedule. This is done by looping over the number of rounds and performing the following operations on the current key value:

      - Converting the key bytes back to an integer using the `from_bytes` method.
      - Performing a left shift by 3 bits on the key value using the `<<` and `>>` operators.
      - XORing the key value with the round number using the `^` operator.
      -	Converting the updated key value to a bytes object using the `to_bytes` method.
      -	Adding the new key bytes to the key schedule list.

5.	The `generate_key_schedule` function then returns the final key schedule list.

6.	The program then defines a function called `xor_shift_encrypt` that takes a plaintext string and a key schedule list as input and returns an encrypted ciphertext string.

7.	The `xor_shift_encrypt` function first initializes an empty string to store the ciphertext.

8.	It then loops over each character in the plaintext string and performs the following operations on each character:

      -	Gets the key bytes for the current round of encryption by taking the modulus of the current loop index with the length of the key schedule list.
      -	Shifts the ASCII code of the current character by the current key byte using the `ord` and `chr` functions.
      -	XORs the shifted ASCII code with the next key byte in the sequence using the `^` operator and `ord` and `chr` functions.
      - Adds the encrypted character to the ciphertext string.

9.	The `xor_shift_encrypt` function then returns the encrypted ciphertext string.

10.	The program then defines a function called `xor_shift_decrypt` that takes a ciphertext string and a key schedule list as input, and returns a decrypted plaintext string.

11.	The `xor_shift_decrypt` function first initializes an empty string to store the plaintext.

12.	It then loops over each character in the ciphertext string and performs the following operations on each character:

       -	Gets the key bytes for the current round of decryption by taking the modulus of the current loop index with the length of the key schedule list.
       -	XORs the ASCII code of the current character with the next key byte in the sequence using the `^` operator and `ord` and `chr` functions.
       -	Shifts the ASCII code of the decrypted character by the current key byte using the `ord` and `chr` functions.
       -	Adds the shifted character to the plaintext string.
    
13.	The `xor_shift_decrypt` function then returns the decrypted plaintext string.

                
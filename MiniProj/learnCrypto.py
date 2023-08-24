#!/usr/bin/env python
# Title: Learning cryptography using python.

import sys
import argparse

__doc__ = '''Welcome to the world of Cryptography.\nHere we will explore the basics of Cryptography.\nOur aim here is simple, that is, to help anyone specially beignners in understanding terms such as encryption, decryption, cipher, dicipher, etc.\nWe will be looking into few basic cryptographics algorithms such as: reverse cipher, Caesar cipher, ROT13, Base64 encryption, XOR cipher, Vignere cipher, RSA algorithms.\n'''

print(__doc__)
print(10 * "******")

# reverse cipher (plain message)
def reverse_cipher(msg):
    translated = '' # to store the cipher text
    i = len(msg) - 1

    while i >= 0:
        translated += msg[i]
        i -= 1

    print(f"The cipher text is : {translated}")

# Caesar cipher (plain message and shift pattern)
def caesar_cipher(msg, sp): 
   result = '' # to store the cipher text
   for i in range(len(msg)):
       char = msg[i]
       if (char.isupper()):
           result += chr((ord(char) + sp - 65) % 26 + 65) # encrypt upper case letters
       else:
           result += chr((ord(char) + sp - 97) % 26 + 97) # encrypt lower case letters
       
   print(result)


# ROT 13
def rot13(msg):
    pass

# Base64 encoding and decoding
def base64(msg):
    pass

# XOR cipher
def xor_cipher(msg):
    pass

# Vignere cipher
def vignere_cipher(msg):
    pass

# RSA algorithm
def rsa(msg):
    pass

################

for i in range(8):
    try:
        print("Lists of cryptographic algorithms:\n  1. Reverse cipher\n  2. Caesar cipher\n  3. ROT 13\n  4. Base64 Encoding & Decoding\n  5. XOR cipher\n  6. Vignere cipher\n  7. RSA Algorithms.\n  8. Exit\n\n")

        choice = int(input("[Choose one of above options] >>> "))

        if choice == 1:
            print(" --- Let's understand Reverse Cipher --- ")
            msg = input("Enter a message you want to cipher:")
            reverse_cipher(msg)
            break

        elif choice == 2:
            print(" --- Let's understand Caesar cipher --- ")
            msg = input("Enter a message you to want to cipher: ")
            sp = int(input("Enter shift pattern: "))
            caesar_cipher(msg, sp)
            break

        elif choice == 3:
            print(" --- Let's understand ROT 13 --- ")
            break
        elif choice == 4:
            print(" --- Let's understand Base64 Encoding and Decoding --- ")
            break
        elif choice == 5:
            print(" --- Let's understand XOR cipher ---")
            break
        elif choice == 6:
            print(" --- Let's understand Vignere cipher --- ")
            break
        elif choice == 7:
            print(" --- Let's understand RSA alogrithm --- ")
            break
        elif choice == 8:
            sys.exit(0)
        else:
            print("[*] Choose correct option from above list...")
            break

    except ValueError:
        print("[**] Input type is not integer.")





#!/usr/bin/env python
# Title: Learning cryptography using python.

import sys
import argparse
import base64
from os import urandom


__doc__ = '''Welcome to the world of Cryptography.\nHere we will explore the basics of Cryptography.\nOur aim here is simple, that is, to help anyone specially beignners in understanding terms such as encryption, decryption, cipher, dicipher, etc.\nWe will be looking into few basic cryptographics algorithms such as: reverse cipher, Caesar cipher, ROT13, Base64 encryption, XOR cipher, Vignere cipher, RSA algorithms.\n'''

print(__doc__)
print(10 * "******")

# reverse cipher (plain message)
def reverse_cipher(msg):
    __doc__ = '''This cipher uses a pattern of reversing the string of plain text to convert as cipher text. '''
    print(__doc__)
    translated = '' # to store the cipher text
    i = len(msg) - 1

    while i >= 0:
        translated += msg[i]
        i -= 1

    print(f"The cipher text is : {translated}")

# Caesar cipher (plain message and shift pattern)
def caesar_cipher(msg, sp):
    __doc__ = '''A simple type of subsitution cipher.
    Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.
    '''
    print(__doc__)
    result = '' # to store the cipher text
    for i in range(len(msg)):
        char = msg[i]
        if (char.isupper()):
            result += chr((ord(char) + sp - 65) % 26 + 65) # encrypt upper case letters
        else:
            result += chr((ord(char) + sp - 97) % 26 + 97) # encrypt lower case letters
       
    print(f"The resulting cipher text: {result}")


# ROT 13
def rot13(msg):
    __doc__= '''Special case of Caesar cipher where shift pattern is 13.'''
    print(__doc__)
    sp = 13 # shift pattern
    caesar_cipher(msg, sp)

# Base64 encoding and decoding
def base64_encode(msg):
    __doc__ = '''Converts binary data into Text format. Primarily used email encryption.
    Also called as Privacy enhanced Electronic Mail (PEM).
    '''
    encoded_data = base64.b64encode(msg)
    print(f"Encoded text with base64 : {encoded_data}")


# Base 64 decoding
def base64_decode(msg):
    __doc__ = ''''''
    print(__doc__)
    
    decoded_data = base64.b64decode(msg)
    print(f"Decoded text using base64: {decoded_data}")

# XOR cipher

def genkey(length: int) -> bytes:
    ''' Generate key.'''
    return urandom(length)

def xor_strings(s, t) -> bytes:
    ''' Concate xor two strings together.'''
    if isinstance(s, str):
        # text strings contain single characters
        return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf-8')
    else:
        # bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])


def xor_cipher(msg):
    __doc__ = '''the simple XOR cipher is a type of additive cipher,[1] an encryption algorithm. XOR is nothing but exclusive disjunction. This algorith requires two parameters, first being plain text and other being key.
    '''
    print(__doc__)
    
    key = genkey(len(msg))
    print(f'Key: {key}')

    cipher_text = xor_strings(msg.encode('utf-8'), key)
    print(f"Converted cipher text is : {cipher_text}")


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
            msg = input("Enter a message you to want to cipher:")
            rot13(msg)
            break
        elif choice == 4:
            print(" --- Let's understand Base64 Encoding and Decoding --- ")

            print("What you want to do:\n")
            print("1. Base64 Encoding\n 2. Base64 Decoding")
            option = int(input("Select from above option: >>>"))
            if option == 1:
                print("--- Base64 encoding ----")
                msg = input("Enter a message you want to encode using base64: ")
                base64_encode(msg)
                break

            elif option == 2:
                print("--- Base64 Decoding ---")
                msg = input("Enter text you want to decode using base64 : ")
                base64_decode(msg)
                break
            break

        elif choice == 5:
            print(" --- Let's understand XOR cipher ---")
            msg = input("Enter a message for converting to cipher text: ")
            xor_cipher(msg)
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





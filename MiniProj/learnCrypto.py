#!/usr/bin/env python
# Title: Learning cryptography using python.

import sys
import argparse
import base64
from os import urandom
from math import sqrt
#required for the sqrt() function, if you want to avoid doing **0.5
import random
#required for randrange
from random import randint as rand




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
    sp = 13 #  fixed shift pattern to 13
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

########### XOR cipher #####################

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


############### Vignere cipher ####################
def generateKey(msg, keyword):
    '''Function to generate the key in a cyclic manner until it's length isn't equal to the length of original text.'''
    key = list(keyword)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def vignere_cipher(msg, key):
    '''Function returning the encrypted text generated with the help of the key.'''
    cipher_text = [] # empty list to store the cipher
    for i in range(len(msg)):
        x = (ord(msg[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

def vignere_decipher(cipher_text, key):
    '''Function to decrypt the vignere cipher and returns original text'''
    original_text = [] # empty list for storing original text
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        original_text.append(chr(x))
    return ("".join(original_text))


##########3 RSA algorithm ###################
# calculate greatest common divisor
def gcd(a, b): 
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# checking if number is PRIME.
def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


#initial two random numbers p,q
p = rand(1, 1000)
q = rand(1, 1000)


def generate_keypair(p, q, keysize):
    # keysize is the bit length of n so it must be in range(nMin,nMax+1).
    # << is bitwise operator
    # x << y is same as multiplying x by 2**y
    # i am doing this so that p and q values have similar bit-length.
    # this will generate an n value that's hard to factorize into p and q.

    nMin = 1 << (keysize - 1)
    nMax = (1 << keysize) - 1
    primes = [2]
    # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
    start = 1 << (keysize // 2 - 1)
    stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while (primes and primes[0] < start):
        del primes[0]

    #choosing p and q from the generated prime numbers.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    #generate public key 1<e<phi(n)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        #as long as gcd(1,phi(n)) is not 1, keep generating e
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        #generate private key
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break

    #public key (e,n)
    #private key (d,n)

    return ((e, n), (d, n))


def encrypt(msg_plaintext, package):
    #unpack key value pair
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext


def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))

######################################################################################################
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
            __doc__ = '''The Vignere cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.
    '''
            print(" --- Let's understand Vignere cipher --- ")
            print(__doc__)
            print(10 * "*")
            
            msg = input("Enter a message in UPPERCASE for encryption:>>> ")
            keyword = input("Enter a key of your choice in UPPERCASE: >>> ")
            # generating key for encrypting or decrypting
            key = generateKey(msg, keyword)

          
            print("What you want to do:\n")
            print("1. Encrypt\n 2. Decrypt")
            opt = int(input("Select on choice from above: >>>"))
            if opt == 1:
                print("--- Encrypting using Vignere cipher ---")
                cipher_text = vignere_cipher(msg, key)
                print(f"Cipher text >>> {cipher_text}")
                break
            elif opt == 2:
                print("---Decrypting Vignere---")
                print("Enter a string in UPPERCASE for decryption:>>> ")
                original_text = vignere_decipher(cipher_text, key)
                print(f"Orignal Text >>> {original_text}")
                break
            break

        elif choice == 7:
            print(" --- Let's understand RSA alogrithm --- ")
            
            bit_length = int(input("Enter bit_length: "))
            
            print("Running RSA...")
            print("Generating public/private keypair...")
            
            public, private = generate_keypair(p, q, 2**bit_length)  # 8 is the keysize (bit-length) value.
            
            print("Public Key: ", public)
            print("Private Key: ", private)
            
            msg = input("Enter a message :>>> ")

            print([ord(c) for c in msg])
            encrypted_msg = encrypt(msg, public)
            
            print("Your Encrypted message: ")
            print(''.join(map(lambda x: str(x), encrypted_msg)))
            
            print("your Decrypted message: ")
            print(decrypt(encrypted_msg, private))


            break

        elif choice == 8:
            sys.exit(0)
        else:
            print("[*] Choose correct option from above list...")
            break

    except ValueError:
        print("[**] Input type is not integer.")





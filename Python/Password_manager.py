pip install pyperclip cryptography

# imports essential tools for a password manager 

import json, hashlib, getpass, os, pyperclip, sys
from cryptography, fernet import Fernet

# json is a library for encoding and decoding data in JSON format 

# hashlib a library for secure hash funstions such as SHA-256 a cryptographic hash functiom
# that produces fixed size (32 byte) hash value from input data of any size

# getpass is a library for secuely handling password prompts without echoing input 
# and showing on the screen -- similar to linux terminal password prompt

# os allows interaction with the OS such as file manipulation 

# pyperlcip is a library for clipboard operations enabling copy paste in a platform 
# independent manner

# sys provides access to various system specific parameters and functions 

# cryptography.fernet cryptography library provides Fernet symmetric-key encryption
# method for securely encrypting and decrypting data 


# create a hash function to hash the master password using SHA-256 algorithm
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()

# now we need a function to generate a key 
# this is used for encrypting and decrypting passwords 
# this has to be the same everytime so we are going to generate it once, store it
# and keep using it 

# Next we use fernet to make it able to encrypt and decrypt passwords and create
# functions for encrypting and decrypting 

# generate a secret key: done only once 
de gen_key():
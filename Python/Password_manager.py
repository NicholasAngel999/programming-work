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
def gen_key():
    return Fernet.generate_key()


# intialise Fernet cipher with provided key
def initialise_cipher(key)
    return Fernet(key)


# function to actually encrypt password 
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()
# this defines a function called encrypt_password which expects 2 inputs 
# password and the cipher 
# password.encode converts the string "mypassword" into bytes that Fernet requires 
# cipher.encrypt fernet encrypts those bytes and produces the encrypted string 
# .decode() converts the encrypted bytes into normal string, easier to store
# return gives encrypted string back to wherever called the function


# function to decrypt password
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# defines function called decrypt_password which requires the input of cipher and
# encrypted password
# cipher.decrypt decrypts the password using fernet 
# .decode() converts back to readable string such as "Mypassword"
# return gives it back to where it was called from


# create a function for owner registration
# saving data in user_data.json
# We will be hashing the password, this is the master password

# function to register you 
def register(username, master_password):
    # encrypt master password before saving it
    hashed_master_password = hash_password(master_password)
    user_data = {'username': username, 'master_password': hashed_master_password}
    file_name = 'user_data.json'
    if os.path.exists(file_name) and os.path.getsize(file_name) ==0:
        with open(file_name, 'w') as file:
            json.dump(user_data, file)
            print("\n[+] Registration complete!\n")

# Define a function called register that takes username and master_password as inputs.
# Hash the master password before saving it.
# Create a dictionary to store user data.
# Define the JSON file where user data will be saved.
# Check if the file exists and is empty before writing.
# Open the file in write mode using a context manager.
# Write the dictionary to the file in JSON format.
# Print a confirmation message.


# create a logging in function 
# this will take the password entered, hash it using the key from before 
# and then compared with the hashed saved mster password and if it matches
# and so does the username access granted 


# log in function
def login(username, entered_password):
    try:
        with open('user_data.json', 'r') as file:
            user_data = json.load(file)
        stored_password_hash = user_data.get('master_password')
        entered_password_hash = hash_password(entered_password)
        if entered_password_hash == stored_password_hash and username == user_data.get('username'):
            print("\n[+] Login Successful..\n")
        else:
            print("\n[-] Invalid login credentials. Please try again")
            sys.exit()
    except Exception:
        print("\n[-] You have not registered. Please regsiter a user.\n")
        sys.exit()




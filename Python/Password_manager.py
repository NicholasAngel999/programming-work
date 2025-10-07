# pip install pyperclip cryptography

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
# \n prints on a new line


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

# funtion log in defined -- requires username and password as input 
# entered password is important as it is being compared to master_password
# opens user_data.json in read only format and will close at end of block
# loads file contents into user_data as a python directory
# stored_password_hash is set to the master_password value from user_data.
# entered_password is hashed with hash_password() for secure comparison.
# checks credentials with what is stored in user_data.json
# prints a message correspondng to the outcome 



# function to view websites saved in password manager 

def view_websites():
    try:
        with open('passwords.json', 'r') as data:
            view = json.load(data)
            print("\n Websites youve saved..\n")
            for x in view:
                print(x['website'])
            print('\n')

    except FileNotFoundError:
        print("\n[-] You have not saved aby passwords!\n")

# define function websites - requires no input
# starts a try block to catch errors that might happen while reading the file
# open passwords.json for reading only - closes with block end - data is a file object you can read from
# view = json.load(data) reads json from file and converts into python objects 
# for x in view -- loop over the elements in view 
# print(x['website']) for each x in the loop print the value at key 'website'
# this assumes each element x is a dict that contains a 'website' key
# except FileNotFoundError if passwords.json doesnt exist run error message



# next we need to generate/load our key 
#load/generate encryption key

key_filename = 'encryption_key.key'
if os.path.exists(key_filename):
    with open(key_filename, 'rb') as key_file:
        key = key_filename.read()
else:
    key = generate_key()
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)

cipher = initialise_cipher(key)

# 1: sets filename used to save and load symmetric encryption key
# 2: checks whether that file already exists if it does load existing key
# 3: opens file safely in read binary mode
# 4: reads the entire contents of teh file into the variable key
# 5: runs the block only if key file doesnt exist
# 6: calls a helper function (like wrapping Fernet.generate_key()) thats makes a new random encrytpion
# 7: opens file in write binary mode - if doesnt exist is created 
# 8: writes the generated key into the file so it can be reused in the future 
# 9: Uses that key to create an encryption/decryption object (most likely Fernet(key) under the hood).


# function to add (save passwords)

def add_password(website, password):
    if not os.path.exists('passwords.json'):
        data = []
    else:
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError: 
            data = []
    encrypted_password = encrypted_password(cipher, password)
    password_entry = {'website': website, 'password': encrypted_password}
    data.append(password_entry)
    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

# check if passwords.json exists
# if passwords.json doesnt exist, initialise it with an empty list
# load existing data from passwords.json
# handle the case where passwords.json is empty or invalid JSON
# encrypt the password
# create a directory to store the websites and passwords 
# save updated list back to passwords.json


# retrieve saved passwords

def get_password(website):
    if not os.path.exists('passwords.json'):
        return None 
    try:
     with open('passwords.json', 'r') as file:
        data = json.load(file)
    except json.JSONDecodeError:
        data = []
    for entry in data:
        if entry['website'] == website:
        decrypt_password = edcrypt_password(cipher, entry['password'])
        return encrypted_password
    return None

# define get_passwords requires an input of a website 
# check if 'passwords.json' exists
# load data from 'passwords.json' 
# everything from try to data = [] makes it loop trhough all websites and check if the required website has already been saved
# if entry['website'] decrypts the passwword if the desired website can be found in saved file
# then returns encrypted_password



# Body/Interface/interaction
# infintie loop to keep the program running until the user chooses to quit 

while True: #loop 
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice:")
    if choice == '1': # for user who want to make account
        file = 'user_data.json'
        if os.path.exists(file) and os.path.getsize(file) !=0:
            print("\n[-] Master user already exisst!![-]\n")
            sys.exit()
        else:
            username = input("Enter you username: ")
            master_password = getpass.getpass("Enter your master password: ")
            login(username, master_password)
    elif choice =='2':
        file = 'user_data.json'
        if os.path.exists(file):
            username = input("Enter your username: ")
            master_password = getpass.getpass("Enter your master password: ")
            login(username, master_password)
        else:
            print("\n[-] You have not registered. Please regsiter account. \n")
            sys.exit()
    # Options after successful login
        while True:
            print("1. Add password")
            print("2. Get password")
            print("3. View saved password")
            print("4. Quit")
            password_choice = input("Enter your choice: ")
            if password_choice == '1':
                website = input("Enter website: ")
                password = getpass.getpass("Enter password: ")
                add_password(website, password)
                print("\n[+] Password added!\n")
            elif password_choice == '2':    # if wanrs to retrieve password
                website = input("Enter website: ")
                decrypted_password = get_password(website)
                if website and decrypted_password:
                    pyperclip.copy(decrypted_password)
                    print(f"\n[+] password for {website}: {decrypted_password}\n[+] Password copied to clipboard.\n")
                else:
                    print("\n[-] Password not foun! Did you save the password?"
                          "\nn[-] Use option 3 to see the websites you saved. \n")
            elif password_choice == '3':
                view_websites()
            elif password_choice == '4':
                break
            elif choice == '3':
                break







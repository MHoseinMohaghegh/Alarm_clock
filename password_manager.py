# Import the necessary module for encryption
from cryptography.fernet import Fernet

'''
# Function to generate and write a new key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

# Function to load the key from the key file


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Load the encryption key
key = load_key()
# Create a Fernet cipher object using the key
fer = Fernet(key)

# Function to view decrypted passwords from the 'passwords.txt' file


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            # Decrypt the password and print the user and decrypted password
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

# Function to add a new password to the 'passwords.txt' file


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        # Encrypt the password and write the account details to the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# Main loop to interactively choose between viewing or adding passwords
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

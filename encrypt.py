import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

# Function to select a key file
def select_file():
    keyroot = tk.Tk()
    keyroot.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

# Select the key file at runtime
keyfile_path = select_file()

# Read the key from the selected file
with open(keyfile_path, 'rb') as filekey:
    key = filekey.read()

def encrypt_files_in_folder(folder_path, key):
    # Generate the encryption cipher using the provided key
    cipher = Fernet(key)
    
    # Ensure the "encrypted" subdirectory exists
    encrypted_folder = os.path.join(folder_path, 'encrypted')
    os.makedirs(encrypted_folder, exist_ok=True)
    
    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Read the contents of the file
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Encrypt the file data
            encrypted_data = cipher.encrypt(file_data)

            # Write the encrypted data to the "encrypted" subdirectory
            encrypted_file_path = os.path.join(encrypted_folder, os.path.basename(file_path))
            with open(encrypted_file_path, 'wb') as f:
                f.write(encrypted_data)

    print("Encryption complete!")

def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

folder_path = select_folder()
encryption_key = key

encrypt_files_in_folder(folder_path, encryption_key)
# Personal Private Encryptor. A simple GUI to encrypt and decrypt files and folders using fernet.
# https://github.com/HarryR275/PersonalPrivateEncryptor/tree/main
# harryrdev@gmail.com

import tkinter as tk
import os
import tkinter.filedialog as filedialog
from cryptography.fernet import Fernet

#----------------- ENCRYPT WINDOW----------------#
# Function to handle the encrypt button click
def openEncryptWindow(key):
    # Toplevel object which will be treated as a new window
    EncryptWindow = tk.Toplevel(window)
    EncryptWindow.title("Encrypt")
    EncryptWindow.geometry("200x200")

    # Create the buttons
    enbutton1 = tk.Button(EncryptWindow, text="Single File", command=lambda:enbutton1_click(key))
    enbutton2 = tk.Button(EncryptWindow, text="Entire Folder", command=lambda:enbutton2_click(key))
 
    # A Label widget to show in toplevel
    tk.Label(EncryptWindow, 
          text ="Encrypt Window").pack()
    
    enbutton1.pack(pady=5)
    enbutton2.pack()

def enbutton1_click(key):
    file_path = filedialog.askopenfilename()
    file_directory = os.path.dirname(file_path)
    if file_path:
        # Perform encryption logic using the selected file
        print("Encrypting file:", file_path)
        cipher = Fernet(key)
    
        # Ensure the "encrypted" subdirectory exists
        encrypted_folder = os.path.join(file_directory, 'encrypted')
        os.makedirs(encrypted_folder, exist_ok=True)

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
    else:
        print("No file selected.")

def enbutton2_click(key):
    folder_path = filedialog.askdirectory()
    if folder_path:
        # Perform encryption logic using the selected file
        cipher = Fernet(key)
    
        # Ensure the "encrypted" subdirectory exists
        encrypted_folder = os.path.join(folder_path, 'encrypted')
        os.makedirs(encrypted_folder, exist_ok=True)

        # Iterate over all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.dirname(file_path) == os.path.join(folder_path, 'encrypted'):
                    continue
                # Rest of the encryption logic goes here

                # Read the contents of the file
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                # Encrypt the file data
                print("Encrypting file:", file_path)
                encrypted_data = cipher.encrypt(file_data)

                # Write the encrypted data to the "encrypted" subdirectory
                encrypted_file_path = os.path.join(encrypted_folder, os.path.basename(file_path))
                with open(encrypted_file_path, 'wb') as f:
                    f.write(encrypted_data)

        print("Encryption complete!")
    else:
        print("No folder selected.")
    #-----------------------------------------#

#----------------- DECRYPT WINDOW----------------#
# Function to handle the decrypt button click
def openDecryptWindow(key):
     
    # Toplevel object which will 
    # be treated as a new window
    DecryptWindow = tk.Toplevel(window)
    DecryptWindow.title("Decrypt")
    DecryptWindow.geometry("200x200")
    tk.Label(DecryptWindow, 
          text ="Decrypt Window").pack()
    #-----------------------------------------#

#----------MAIN WINDOW-----------------------#
def button1_click():
    # Validating the selected key file. If it is, call the encrypt function.
    key_file = input_entry.get()
    if os.path.isfile(key_file):
        filesize = os.path.getsize(key_file)
        if filesize == 44:
            with open(key_file, 'rb') as filekey:
                key = filekey.read()
            print("Encrypt Stuff Here!")
            openEncryptWindow(key)
            # Encrypt Stuff Here!
        else:
            print("Invalid key file!")
    else:
        print("Key file does not exist!")

def button2_click():
    # Validating the selected key file. If it is, call the decrypt function.
    key_file = input_entry.get()
    if os.path.isfile(key_file):
        filesize = os.path.getsize(key_file)
        if filesize == 44:
            with open(key_file, 'rb') as filekey:
                key = filekey.read()
            print("Decrypt Stuff Here!")
            openDecryptWindow(key)
            # Decrypt Stuff Here!
        else:
            print("Invalid key file!")
    else:
        print("Key file does not exist!")

# Create the main window
window = tk.Tk()
# window title and dimension
window.title("Personal Private Encryptor")
# Set geometry (widthxheight)
window.geometry('350x200')

def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'

input_path = tk.Label(window, text="Key File:")
input_entry = tk.Entry(window, text="", width=40)
browse1 = tk.Button(window, text="Browse", command=input)

# Create the buttons
button1 = tk.Button(window, text="Encrypt", command=button1_click)
button2 = tk.Button(window, text="Decrypt", command=button2_click)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)
spacer1 = tk.Label(window, text="")
# Add the buttons to the window
spacer1.pack()  
button1.pack(pady=5)
button2.pack()
#-----------------------------------------#

# Start the main loop
window.mainloop()
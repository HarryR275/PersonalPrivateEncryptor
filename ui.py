# Personal Private Encryptor. https://github.com/HarryR275/PersonalPrivateEncryptor/tree/main
# harryrdev@gmail.com

import tkinter as tk
import os
import tkinter.filedialog as filedialog
from cryptography.fernet import Fernet

#----------------- ENCRYPT WINDOW----------------#
# Function to handle the encrypt button click
def openEncryptWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    EncryptWindow = tk.Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    EncryptWindow.title("Encrypt")
 
    # sets the geometry of toplevel
    EncryptWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    tk.Label(EncryptWindow, 
          text ="Encrypt Window").pack()
    #-----------------------------------------#

#----------------- DECRYPT WINDOW----------------#
# Function to handle the decrypt button click
def openDecryptWindow():
     
    # Toplevel object which will 
    # be treated as a new window
    DecryptWindow = tk.Toplevel(window)
 
    # sets the title of the
    # Toplevel widget
    DecryptWindow.title("Decrypt")
 
    # sets the geometry of toplevel
    DecryptWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
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
            print("Encrypt Stuff Here!")
            openEncryptWindow()
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
            print("Decrypt Stuff Here!")
            openDecryptWindow()
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
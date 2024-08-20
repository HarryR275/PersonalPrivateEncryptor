import tkinter as tk
import os
import tkinter.filedialog as filedialog

def button1_click():
    # Validating the selected key file. If it is, call the encrypt function.
    key_file = input_entry.get()
    if os.path.isfile(key_file):
        filesize = os.path.getsize(key_file)
        if filesize == 44:
            print("Encrypt Stuff Here!")
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

# Start the main loop
window.mainloop()
from cryptography.fernet import Fernet
import os.path

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)

root_dir = r"Z:\Photos"

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        output1 = os.path.join(directory, file)
        if output1.endswith("crypt"):
            print(output1, " skipping")
        else:
            print(output1)
            # opening the original file to encrypt
            with open(output1, 'rb') as file1:
                original = file1.read()
                newname = ''.join(output1 + 'crypt')
                if os.path.isfile(newname):
                    print("ok")
                else:
                    # encrypting the file
                    encrypted = fernet.encrypt(original)

                    # opening the file in write mode and

                    # writing the encrypted data
                    with open(newname, 'xb') as encrypted_file:
                        encrypted_file.write(encrypted)

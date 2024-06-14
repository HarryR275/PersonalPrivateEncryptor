from cryptography.fernet import Fernet
import os
# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)


root_dir = '/Users/username/encrypted'

for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        output1 = os.path.join(directory, file)
        print(output1)
# opening the original file to encrypt
        with open(output1, 'rb') as enc_file:
            original = enc_file.read()
# encrypting the file
        decrypted = fernet.decrypt(original)

# opening the file in write mode and
        newname = output1[:-5]
# writing the encrypted data
        with open(newname, 'xb') as dec_file:
            dec_file.write(decrypted)

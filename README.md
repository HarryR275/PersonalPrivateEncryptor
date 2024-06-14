# PersonalPrivateEncryptor
I've been trying to develop this in what little free time I've had recently: Encrypting files in a folder at rest BEFORE transit. Why? I feel like there are always going to be privacy concerns when transmitting/storing data ANYWHERE, including public cloud. I'm going to focus this toward S3 at some point, but now, in its infancy, this is brand-agnostic.

each file is encrypted, and then the filename is appended with "crypt" on the end.

New Initial Commit:
encrypt.py has a "root_dir" variable, this is the folder whose contents will be encrypted.
decrypt.py does exactly what you think it does.
filekey.key a fernet key as a flat file. ONLY USE THIS TO TEST WITH. THIS KEY IS PUBLIC, AND THEREFORE, ANYONE CAN DECRYPT YOUR FILES. To generate one of your own, go somewhere like fernetkeygen.com.


TODO:
Create a script to delete the originals, if wanted (with warnings).
Create one to delete the encrypted ones, so after upload, they can free the space if desired.
Graphically allow user to choose folders for encrypt and decrypt.
Be perhaps more verbose on the key creation/use.

# PersonalPrivateEncryptor
Encrypting files in a folder at rest BEFORE transit. Why? Well, think about private things; family photos, genealogy, documents, etc.
I feel like there are always going to be privacy concerns when transmitting/storing data ANYWHERE, including public cloud. I'm going to focus this toward S3 at some point, but now, in its infancy, this is brand-agnostic.

**IMPORTANT** This project is really more for my own benefit; I'm trying to learn/develop more, and transition into a development role. As such, I cannot stress to you enough: I'm not responsible for anything that comes from you using this application. I believe in it, it'll work, but I'm just not in a position to state that your data stays private using it.

I'm going to use the readme as a Changelog for now. Perhaps if this was a bigger project (or somehow grows to that level) I will break it out into a changelog.md:

08/20/2024:
As of today, I'm creating the GUI for this in ui.py. Later, I'll be adding the encryption/decryption (what was initially multiple python files) but for now, ui.py is where everything will come together.

08/21/2024:
Good sized update here. The Encrypt side of the application is running pretty well. User can choose a single file or a folder.

**TODO:**
The Folder encrypt/decrypt needs an option for the user to select recursive or no.
Make the forms close.
Do better error handling, like when the key isn't chosen yet by the user. Currently just displaying in the console, I'd rather it flash something red in the form/window.
I'd like to obscure the filenames and/or extensions. One point in cryptography is that if you know what a portion of the end result should be, it's incredibly easier to crack. So, if I know that there's a bunch of .jpg's in a folder, I can use that to help solve the cipher. I'm not sure how realistic that is with current encryption technologies, but the feasibility is nonzero.
At some point, I should be able to upload to S3 from within the application directly. For now, it's manual and I don't mind the extra bit of control there.

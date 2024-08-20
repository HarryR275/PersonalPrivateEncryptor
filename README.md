# PersonalPrivateEncryptor
I've been trying to develop this in what little free time I've had recently: Encrypting files in a folder at rest BEFORE transit. Why? Well, think about private things; family photos, genealogy, documents, etc.
I feel like there are always going to be privacy concerns when transmitting/storing data ANYWHERE, including public cloud. I'm going to focus this toward S3 at some point, but now, in its infancy, this is brand-agnostic.

**IMPORTANT** This project is really more for my own benefit; It's a lot about me growing as a developer and moving away from the MSP space. As such, I cannot stress to you enough: I'm not responsible for anything that comes from you using this application. I believe in it, it'll work, but I'm just not in a position to state that your data stays private using Fernet keys.


08/20/2024:
As of today, I'm creating the GUI for this in ui.py. Later, I'll be adding the encryption/decryption (what was initially multiple python files) but for now, ui.py is where everything will come together.

**TODO:**
Fill the content of Encrypt/Decrypt tk windows. There are still a couple of user-selectable options.
Get this baby to sleep more.
At some point, I should be able to upload to S3 from within the application directly. For now, it's manual and I don't mind the extra bit of control there.

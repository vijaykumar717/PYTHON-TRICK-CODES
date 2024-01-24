
from cryptography.fernet import Fernet

 # Generate a random encryption key
key = Fernet.generate_key()

 # Create a Fernet encryption object
cipher_suite = Fernet(key)

 # Data to be encrypted
data_to_encrypt = b"This is a secret message."

 # Encrypt the data
encrypted_data = cipher_suite.encrypt(data_to_encrypt)
print("Encrypted Data:", encrypted_data)

 # Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)
print("Decrypted Data:", decrypted_data.decode())


##data1= {mobile no:'9655052530'}

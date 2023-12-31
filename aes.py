from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_ecb_encrypt(key, plaintext):
	plaintext_bytes = plaintext.encode('utf-8')
	padder = padding.PKCS7(algorithms.AES.block_size).padder()
	padded_plaintext = padder.update(plaintext_bytes) + padder.finalize()
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
	encryptor = cipher.encryptor()
	return encryptor.update(padded_plaintext) + encryptor.finalize()

def aes_ecb_decrypt(key, ciphertext):
	cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
	decryptor = cipher.decryptor()
	decrypted_bytes = decryptor.update(ciphertext) + decryptor.finalize()
	unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
	unpadded_plaintext = unpadder.update(decrypted_bytes) + unpadder.finalize()
	return unpadded_plaintext.decode('utf-8')

def aes_cbc_encrypt(key, plaintext, iv):
	plaintext_bytes = plaintext.encode('utf-8')
	padder = padding.PKCS7(algorithms.AES.block_size).padder()
	padded_plaintext = padder.update(plaintext_bytes) + padder.finalize()
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	encryptor = cipher.encryptor()
	return encryptor.update(padded_plaintext) + encryptor.finalize()

def aes_cbc_decrypt(key, ciphertext, iv):
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
	decryptor = cipher.decryptor()
	decrypted_bytes = decryptor.update(ciphertext) + decryptor.finalize()
	unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
	unpadded_plaintext = unpadder.update(decrypted_bytes) + unpadder.finalize()
	return unpadded_plaintext.decode('utf-8')

def des_encrypt(message, key, mode):
	padded_message = pad(message, DES.block_size)
	if mode == 'ECB':
		cipher = DES.new(key, DES.MODE_ECB)
	elif mode == 'CBC':
		cipher = DES.new(key, DES.MODE_CBC, iv)
		encrypted_message = iv + cipher.encrypt(padded_message)  # Prepend IV for CBC mode
		return encrypted_message
	else:
		raise ValueError("Unsupported mode")
	return cipher.encrypt(padded_message)

def des_decrypt(encrypted_message, key, mode):
	if mode == 'ECB':
		cipher = DES.new(key, DES.MODE_ECB)
	elif mode == 'CBC':
		iv = encrypted_message[:DES.block_size]  # Extract the IV from the beginning
		encrypted_message = encrypted_message[DES.block_size:]
		cipher = DES.new(key, DES.MODE_CBC, iv)
	else:
		raise ValueError("Unsupported mode")
	decrypted_message = cipher.decrypt(encrypted_message)
	unpadder = padding.PKCS7(DES.block_size).unpadder()
	unpadded_plaintext = unpadder.update(decrypted_message) 
	return unpadded_plaintext.decode('utf-8')

if __name__ == "__main__":
	# AES TESTING
	"""
	key_hex = "00112233445566778899aabbccddeeff" # Example for AES-128
	iv_hex = "0102030405060708090a0b0c0d0e0f10"
	key_bytes = bytes.fromhex(key_hex)
	iv_bytes = bytes.fromhex(iv_hex)
	plaintext = "Hello, world!"
	#print("Plaintext:", plaintext)
	encrypted = aes_ecb_encrypt(key_bytes, plaintext) 
	#print("Encrypted (ECB):", encrypted)
	decrypted = aes_ecb_decrypt(key_bytes, encrypted)
	print("Decrypted (ECB):", decrypted)
	encrypted2 = aes_cbc_encrypt(key_bytes, plaintext, iv_bytes)
	decrypted2 = aes_cbc_decrypt(key_bytes, encrypted2, iv_bytes)
	print("Decrypted (CBC):", decrypted2)
	encrypted = aes_ecb_encrypt(key_bytes, plaintext) 
	decrypted = aes_ecb_decrypt(key_bytes, encrypted)
	print("Decrypted (ECB):", decrypted)
	encrypted2 = aes_cbc_encrypt(key_bytes, plaintext, iv_bytes)
	print("Encrypted (CBC):", encrypted2)
	decrypted2 = aes_cbc_decrypt(key_bytes, encrypted2, iv_bytes)
	print("Decrypted (CBC):", decrypted2)
	"""
	# DES TESTING
	key = get_random_bytes(8)  # DES key must be 8 bytes long
	iv = get_random_bytes(DES.block_size)  # IV must be 8 bytes long for DES
	"""
	plaintext = b'Hello with ECB'
	encrypted4 = des_encrypt(plaintext, key, mode='ECB')
	decrypted4 = des_decrypt(encrypted4, key, mode='ECB')
	print('Decrypted:',decrypted4)
	"""
	plaintext = b'Hello with CBC'
	print('Plaintext:', plaintext)
	encrypted5 = des_encrypt(plaintext, key, mode='CBC')
	print('Encrypted:',encrypted5)
	decrypted5 = des_decrypt(encrypted5, key, mode='CBC')
	"""
	print('Decrypted:',decrypted5)
	"""

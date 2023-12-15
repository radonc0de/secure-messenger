import math_helpers

def text_to_bits(plaintext):
	bits = bin(int.from_bytes(plaintext.encode('utf-8', 'surrogatepass'), 'big'))[2:]
	return bits.zfill(8 * ((len(bits) + 7) // 8))

def bits_to_text(bits):
	n = int(bits, 2)
	byte_number = n.bit_length() + 7 // 8
	binary_array = n.to_bytes(byte_number, "big")
	return binary_array.decode('utf-8', 'surrogatepass')

def encrypt_bits(bitstream, keystream):
	plaintext_bytes = int(bitstream, 2).to_bytes((len(bitstream) + 7) // 8, byteorder='big')
	keystream_bytes = int(keystream, 2).to_bytes((len(keystream) + 7) // 8, byteorder='big')
	ciphertext_bytes = math_helpers.xor_bytes(plaintext_bytes, keystream_bytes)
	ciphertext_bits = ''.join(f'{byte:08b}' for byte in ciphertext_bytes)
	return ciphertext_bits 

def decrypt_bits(ciphertext_bits, keystream):
	ciphertext_bytes = int(ciphertext_bits, 2).to_bytes((len(ciphertext_bits) + 7) // 8, byteorder='big')
	keystream_bytes = int(keystream, 2).to_bytes((len(keystream) + 7) // 8, byteorder='big')
	plaintext_bytes = math_helpers.xor_bytes(ciphertext_bytes, keystream_bytes)
	plaintext_bits = ''.join(f'{byte:08b}' for byte in plaintext_bytes)
	return plaintext_bits

"""
def image_to_bits(image_path):

def bits_to_image(bits):
"""

if __name__ == "__main__":
	plaintext = "Hello World!"
	key = "Use me for encryption!!!"
	print('Plaintext:', plaintext)
	print('Key:', key)
	bits = text_to_bits(plaintext)
	print('Plaintext as bits:', bits)
	keybits = text_to_bits(key)
	print('Key as bits:', keybits)
	encrypted = encrypt_bits(bits, keybits)
	print('Encrypted bits:', encrypted)
	decrypted = decrypt_bits(encrypted, keybits)
	print('Decrypted bits:', decrypted)
	words = bits_to_text(decrypted)
	print('Decrypted plaintext:', words)

	plaintext = "I love stream ciphers!"
	key = "eifjcasdasbfvugterkglrasjdkahsdasjkvhklgktgnnblbvdfvvfasdasebirdkev"
	print('Plaintext:', plaintext)
	print('Key:', key)
	bits = text_to_bits(plaintext)
	print('Plaintext as bits:', bits)
	keybits = text_to_bits(key)
	print('Key as bits:', keybits)
	encrypted = encrypt_bits(bits, keybits)
	print('Encrypted bits:', encrypted)
	decrypted = decrypt_bits(encrypted, keybits)
	print('Decrypted bits:', decrypted)
	words = bits_to_text(decrypted)
	print('Decrypted plaintext:', words)

	plaintext = "Can AES encrypt as good as me?"
	key = "asdkjh245238940237423jkha8789f723jkh242389798dsfjkh2342348497hj"
	print('Plaintext:', plaintext)
	print('Key:', key)
	bits = text_to_bits(plaintext)
	print('Plaintext as bits:', bits)
	keybits = text_to_bits(key)
	print('Key as bits:', keybits)
	encrypted = encrypt_bits(bits, keybits)
	print('Encrypted bits:', encrypted)
	decrypted = decrypt_bits(encrypted, keybits)
	print('Decrypted bits:', decrypted)
	words = bits_to_text(decrypted)
	print('Decrypted plaintext:', words)
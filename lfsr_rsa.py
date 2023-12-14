import random
import math_helpers

class LFSR_RSA:
	def __init__(self, p=102188617217178804476387977160129334431745945009730065519337094992129677228373, alpha=2):
		self.p = p
		self.alpha = alpha

	def gen_lfsr_key(self, seed, taps, n):
		seed_length = seed.bit_length()
		print('seed length', seed_length)
		lfsr = seed
		period = 0
		key = []

		while period < n:
			bit = 0
			for t in taps:
				bit ^= (lfsr >> t) & 1
			lfsr = (lfsr >> 1) | (bit << (seed_length - 1))
			key.append(str(lfsr & 1))
			period += 1
		return ''.join(key)

	def generate_keypair(self, p, q):
		if not (math_helpers.is_prime(p) and math_helpers.is_prime(q)):
			raise ValueError('Both numbers must be prime.')
		elif p == q:
			raise ValueError('p and q cannot be equal')
		
		n = p * q
		phi = (p-1) * (q-1)

		e = random.randrange(1, phi)

		g = math_helpers.gcd(e, phi)
		while g != 1:
			e = random.randrange(1, phi)
			g = math_helpers.gcd(e, phi)

		d = math_helpers.multiplicative_inverse(e, phi)

		self.rsa_public = (e, n)
		self.rsa_private = (d, n)
	
	def saveOtherPublic(self, otherPublic):
		self.rsa_otherPublic = otherPublic

	def encrypt(self, plaintext):
		key, n = self.rsa_otherPublic
		cipher = [(ord(char) ** key) % n for char in plaintext]
		return cipher

	def decrypt(self, ciphertext):
		key, n = self.rsa_private
		plain = [chr((char ** key) % n) for char in ciphertext]
		return ''.join(plain)

# For Testing
if __name__ == "__main__":
	u1 = LFSR_RSA()
	u2 = LFSR_RSA()
	lfsr_key = u1.gen_lfsr_key(0b1001010010010011, [0, 5,11,13, 15], 32)
	print(lfsr_key)
	p = 7919
	q = 613
	u1.generate_keypair(p, q)
	u2.generate_keypair(p, q)
	print("Keypairs generated.")
	u1.saveOtherPublic(u2.rsa_public)
	print("Encrypting LFSR key...")
	encrypted_key = u1.encrypt(lfsr_key)
	print(encrypted_key)
	decrypted_key = u2.decrypt(encrypted_key)
	print(decrypted_key)





import random
import math
import math_helpers

class LFSR_RSA:
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

	def rsa_generate_key(self, p, q):
		n = p * q
		phi_n = (p - 1) * (q - 1)
		e = random.randint(2, phi_n - 1)
		while math.gcd(e, phi_n) != 1:
			e = random.randint(2, phi_n - 1)
		d = math_helpers.multiplicative_inverse(e, phi_n)
		self.rsa_public = (e, n)
		self.rsa_private = (d, n)

	def encrypt(self, plaintext):
		key, n = self.rsa_otherPublic
		joined = int(plaintext, 2)
		cipher = math_helpers.exponentiation(joined, key, n)
		return cipher

	def decrypt(self, ciphertext):
		key, n = self.rsa_private
		plain = bin(math_helpers.exponentiation(ciphertext, key, n))
		return ''.join(plain)

	def saveOtherPublic(self, otherPublic):
		self.rsa_otherPublic = otherPublic

# For Testing
if __name__ == "__main__":
	u1 = LFSR_RSA()
	u2 = LFSR_RSA()
	lfsr_key = u1.gen_lfsr_key(0b1001010010110011, [0, 5,11,13, 15], 16)
	print('LFSR Key', lfsr_key)
	p = 102188617217178804476387977160129334431745945009730065519337094992129677228373
	q = 106702241438602472124058018963858502139712770962512057673947766764984716787727
	u1.rsa_generate_key(p, q)
	u2.rsa_generate_key(p, q)
	print("Keypairs generated.")
	u1.saveOtherPublic(u2.rsa_public)
	print("Encrypting LFSR key...")
	encrypted_key = u1.encrypt(lfsr_key)
	print('Encrypted key:', bin(encrypted_key))
	decrypted_key = u2.decrypt(encrypted_key)
	print('Decrypted key:', decrypted_key)





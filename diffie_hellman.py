import random

class DiffieHellman:
	def __init__( self, secret, p=102188617217178804476387977160129334431745945009730065519337094992129677228373, alpha=2):
		self.p = p
		self.alpha = alpha
		self.secret = secret
		self.public = (self.alpha ** self.secret) % self.p
		self.sharedSecret = 0

	def findSharedSecret(self, otherPublic):
		self.sharedSecret = (otherPublic ** self.secret) % self.p


# For Testing
if __name__ == "__main__":
	u1_secret = random.randint(0,100)
	u2_secret = random.randint(0,100)
	u1 = DiffieHellman(secret=u1_secret)
	u2 = DiffieHellman(secret=u2_secret)
	print("U1 public:", u1.public)
	print("U2 public:", u2.public)
	u1.findSharedSecret(u2.public)
	u2.findSharedSecret(u1.public)
	print("U1 computed shared secret:", u1.sharedSecret)
	print("U2 computed shared secret:", u2.sharedSecret)







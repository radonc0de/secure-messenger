import random

class DiffieHellman:
	def __init__( self, p=102188617217178804476387977160129334431745945009730065519337094992129677228373, alpha=2, secret=random.randint(0,100)):
		self.p = p
		self.alpha = alpha
		self.secret = secret
		self.public = (self.alpha ** self.secret) % self.p
		self.sharedSecret = 0

	def findSharedSecret(self, otherPublic):
		self.sharedSecret = (otherPublic ** self.secret) % self.p


# For Testing
if __name__ == "__main__":
	u1 = DiffieHellman(23, 5, 4)
	u2 = DiffieHellman(23, 5, 3)
	print(u1.public)
	print(u2.public)
	u1.findSharedSecret(u2.public)
	u2.findSharedSecret(u1.public)
	print(u1.sharedSecret)
	print(u1.sharedSecret)







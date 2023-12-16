from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

def generate_keys():
	private_key = rsa.generate_private_key(
		public_exponent=65537,
		key_size=2048,
		backend=default_backend()
	)
	public_key = private_key.public_key()
	return private_key, public_key

def sign_document(document, private_key):
	signature = private_key.sign(
		document,
		padding.PSS(
			mgf=padding.MGF1(hashes.SHA256()),
			salt_length=padding.PSS.MAX_LENGTH
		),
		hashes.SHA256()
	)
	return signature

def verify_signature(document, signature, public_key):
	try:
		public_key.verify(
			signature,
			document,
			padding.PSS(
				mgf=padding.MGF1(hashes.SHA256()),
				salt_length=padding.PSS.MAX_LENGTH
			),
			hashes.SHA256()
		)
		return "Verification Successful"
	except InvalidSignature:
		return "Verification Failed"

private_key, public_key = generate_keys()
document = b"Original Document"
print('Document before signing:', document)
signature = sign_document(document, private_key)
print('Signature:', signature)
verification_result = verify_signature(document, signature, public_key)
print("Verification of original document:", verification_result)
modified_document = document + b'sdlkjfsldkfjs'
print('Modified Document:', modified_document)
verification_result = verify_signature(modified_document, signature, public_key)
print("Verification of modified document:", verification_result)

import random
import os

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def exponentiation(m, e, n):
	result = 1
	m = m % n
	while e > 0:
		if e % 2:  # If e is odd, multiply m with the result
			result = (result * m) % n
		e = e // 2  # Reduce e by half
		m = pow(m, 2, n)
		#m = (m * m) % n  # Square m
	return result

def xor_bytes(bytes1, bytes2):
	return bytes(a ^ b for a, b in zip(bytes1, bytes2))
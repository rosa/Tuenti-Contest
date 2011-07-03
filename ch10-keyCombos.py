#!/usr/bin/python
import sys
import random

# The Miller-Rabin primality test
def toBinary(n):
	r = []
	while (n > 0):
		r.append(n % 2)
		n = n / 2
	return r


# test(a, n) -> bool Tests whether n is complex.
# 
#   Returns:
#     - True, if n is complex.
#     - False, if n is probably prime.
def test(a, n):
	b = toBinary(n - 1)
	d = 1
	for i in xrange(len(b) - 1, -1, -1):
		x = d
		d = (d * d) % n
		if d == 1 and x != 1 and x != n - 1:
			return True # Complex
		if b[i] == 1:
			d = (d * a) % n
	if d != 1:
		return True # Complex
	return False # Prime


# MillerRabin(n, s = 1000) -> bool Checks whether n is prime or not
# 
# Returns:
#   - True, if n is probably prime.
#   - False, if n is complex.
def MillerRabin(n, s = 6):
	for j in xrange(1, s + 1):
		a = random.randint(1, n - 1)
		if (test(a, n)):
			return False # n is complex
	return True # n is prime


primesKeys = {}
nprime = 1

# prime generator
# returns a prime number greater than n
def nextPrime(n):
	res = n + 1 
	while not MillerRabin(res):
		res += 1
	return res


# return a hashcode that doesn't depend on the order
# use prime numbers, one prime pi for each key ki
# the hash code is p1*p2...pn, for keys k1,k2,..kn
def hashcode(combo):
	global nprime
	hashcode = 1
	for i in combo:
		if i in primesKeys:
			hashcode *= primesKeys[i]
		else:
			nprime = nextPrime(nprime)
			hashcode *= nprime
			primesKeys[i] = nprime
	return hashcode
	

# read number of combos
n = int(sys.stdin.readline())

# read and store combos
combos = {}
for i in xrange(n):
	combo = (sys.stdin.readline()).split()
	action = sys.stdin.readline()
	combos[hashcode(combo)] = action.strip()

# another option should be just ordering the combos, but this should
# be faster if there are an insanely huge amount of test cases, as you
# would have already generated all the hashes and the primes
	
# read number of test cases
t = int(sys.stdin.readline())

# read and process test cases
for i in xrange(t):
	case = (sys.stdin.readline()).split()	
	hashcase = hashcode(case)
	if hashcase in combos:
		print combos[hashcase]
	else:
		print ''
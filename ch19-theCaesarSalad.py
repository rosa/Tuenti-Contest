#!/usr/bin/python
import sys
import os
from Crypto.Cipher import DES
import base64


# 1's complement
def c1(x):
	binx = "".join([str((x >> y) & 1) for y in range(7, -1, -1)])
	binx = str(int(binx))
	res = ''
	for c in binx:
		if c == '0': 
			res += '1'
		else:
			res += '0'
	return eval('0b'+res)


# arghf..
# What if this XOR was smarter?
# If the keyed XOR is the one used in World of Warcraft 
# realm server communication encryption? 
# translation of a Java function doing exactly that
def xorWoW(data, key):
	m_cData = data
	m_cKey  = map(ord,list(key))
	keyPointer = 0;
	keyPointerAdd = 0;
	for i in range(len(m_cData)):
		keyPointerAdd = m_cData[i]
		m_cData[i] = m_cData[i] ^ m_cKey[keyPointer]
		keyPointer = keyPointer + keyPointerAdd
		keyPointer = keyPointer % len(m_cKey)
	return m_cData
	
#  us = tuenti
key = "tuenti" 

# read input
for line in sys.stdin:
	line = base64.b64decode(line)
	
	# DES cipher (us in 56)
	# key with padding for DES
	uskey = key + '\x00\x00'
	descipher = DES.new(uskey, DES.MODE_ECB)
	line = descipher.decrypt(line)
	
	# 1's complement (34 = 29)
	line = map(c1, map(ord, line))
	
	# XOR from WoW 
	line = xorWoW(line, key)

	# the fourth key lies in the salad
	# for i in xrange(127):
	# 	lineDec = map(lambda x: (x+i)%127, line)
	# 	print ''.join(map(chr,lineDec))	

	# very entertaining, scrolling and looking at ramdon strings here
	
	# line = map(lambda x: (x+107)%127, line)
	# print ''.join(map(chr,line))	


# and at the end, just reply to: 156 * -4
for line in sys.stdin:
	print 156 * -4
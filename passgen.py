#!/usr/bin/python

import random,sys

def generate(length):
	alphabet = "abcdefghjkmnpqrstuvwxyz"
	upperalphabet = alphabet.upper()
	pw_len = length
	pwlist = []

	for i in range(pw_len//3):
		pwlist.append(alphabet[random.randrange(len(alphabet))])
		pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
		pwlist.append(str(random.randrange(10)))
	for i in range(pw_len-len(pwlist)):
		pwlist.append(alphabet[random.randrange(len(alphabet))])

	random.shuffle(pwlist)
	pwstring = "".join(pwlist)

	print(pwstring)

if __name__ == '__main__':

	global length
	length = 8

	if len(sys.argv) > 1: 
		length = int(sys.argv[1])
	try:
		generate(length)
	except BaseException as e:
		print "Something went wrong: %s" % (e)

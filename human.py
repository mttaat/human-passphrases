#!/usr/bin/python3
#
# Copyright (c) 2019 mttaat <mttaat@protonmail.com>. All Rights Reserved.
# This file licensed under the GPLv3
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# human.py v0.1
# human-readable passphrase generator
# usage: $ python human.py <length>
#
# # # # # # # #
# This script utilizes /usr/share/dict/words file under Linux
# to provide a passphrase of desired length.
# I've found a tool like this useful in situations where I am 
# not able to copy-paste generated passwords (ie: when working 
# across systems, or on mobile devices). The human-readability 
# factor allows for easier typing (and perhaps memorization) 
# of longer, relatively-secure passphrases.
#
# # # # # # # # 
# *NSFW NOTE*
# This script does no filtering of the words used, so if your
# /usr/share/dict/words contains filthy language then so may
# your generated passphrases.
#
# @mttaat
# https://mttaat.net
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import sys
import os
import random
import string

phraselen=16
if (len(sys.argv) <2):
	print("no argument supplied, using phrase length " + str(phraselen))
elif (int(sys.argv[1]) < phraselen):
	print("minimum recommended phrase length is 16, using 16...")
else:
	phraselen = int(sys.argv[1])

wordspath='/usr/share/dict/words'
if os.path.exists(wordspath):
	wordsfile=open(wordspath,'r')
else:
	print("words file not found, please supply with the command line argument")
	exit()

wordslist=wordsfile.readlines()

def genphrase(phraselen, wordslist):
	minlen=4
	phrase=""
	stringlen = phraselen
	while stringlen > 0:
		if stringlen<=minlen*2:
			wordlen=stringlen
		else:
			wordlen=random.randint(minlen,minlen*2) 
		stringlen=stringlen-wordlen
		wordlen=wordlen-1
		if wordlen<minlen:
			# leftovers too small, trying again...
			genphrase(phraselen, wordslist)
			return
		pool=[]
		for word in wordslist:
			if (string.find(word, "'") != -1):
				continue
			word=word.strip()
			if (len(word) == wordlen):
				pool.append(word)
		wordindex=random.randint(0,len(pool)-1)
		phrase=phrase + " " + pool[wordindex]
	if (len(phrase) != phraselen):
		# phrase too small, trying again...
		genphrase(phraselen, wordslist)
		return
	print(phrase)

genphrase(phraselen, wordslist)

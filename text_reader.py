#!/usr/bin/python

from sys import *
from collections import Counter

script, filename = argv

in_file = open(filename)
indata = in_file.read()
words = indata.split(' ')

print indata # Remove from final
print words # Remove from final
print "We are going to count the number of words in the file:", filename
print "The number of bytes in the file :", len(indata)

number_words = len(words)

print number_words
count = Counter(words)
print count

print "The top ten most used words are:", count[0,9]
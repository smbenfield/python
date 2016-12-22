#!/usr/bin/python/LPtHW
# python ex33a.py

i = 6
d = 1
numbers =[]

def count(i, d):
	for i in range (i,i+6):
		print "at the top i is %d" % i
		numbers.append(i)

		print "Numbers now:", numbers
		print" At the bottom i is %d." % i

count(i, d)

print "The numbers: "

for num in numbers:
	print num
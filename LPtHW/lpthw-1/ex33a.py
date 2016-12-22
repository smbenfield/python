#!/usr/bin/python/LPtHW
# python ex33a.py

i = 6
d = 3
numbers =[]

def count(i, d):
	while i < (d * 4):
		print "at the top i is %d" % i
		numbers.append(i)
		
		i = i + d
		print "Numbers now:", numbers
		print" At the bottom i is %d." % i

count(i, d)

print "The numbers: "

for num in numbers:
	print num
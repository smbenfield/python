#!/usr/bin/python

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() # pop(more_stuff)
	print "Adding: ", next_one
	stuff.append(next_one) # append(next_one) to the end of more_stuff
	print "There are %d items now." % len(stuff) # counts number of items

print "There we go:", stuff

print "Let's do some more things with stuff."

print stuff[1] # Prints item at index 1 (second item)
print stuff[-1] # whoa! fancy - Prints item at index -1
print stuff.pop() # pop(stuff)
print ' '.join(stuff) # what? cool! - Joins items in stuff with spaces in between
print '#'.join(stuff[3:5]) # super stellar! # joins items at 3 and 5 with a #
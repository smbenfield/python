#!/usr/bin/python

# defines the cheese_and_crackers function and 
# assigns the variables cheese_count and boxes_of_crackers)

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
# feeds the numbers into the function as the two arguments it asks for	
print "we can just give the function numbers directly:"
cheese_and_crackers(20,30)
# assigns values to the variables
print "OR, we can use variables from our script;"
amount_of_cheese = 10
amount_of_crackers = 50
# feeds the numbers into the function as variables that fulfill the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#feeds the numbers into the function, but does math beforehand
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# mixes variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight_lbs = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

weight_kgs = weight_lbs * 2.2

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight_lbs
print "He's %d kilograms in mass." % weight_kgs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight_lbs, age + height + weight_lbs)
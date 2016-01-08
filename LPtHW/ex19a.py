#!/usr/bin/python
# ./ex19a.py Shelby

from sys import argv

script, name = argv
prompt = '>>'

subtotal_smooches = 0

def s_p_math():
	subtotal_smooches = 0
	print "How many smooches did you have yesterday?"
	accrued_smooches = int(raw_input(prompt))
	
	print "How many smooches have you gotten today?"
	today_smooches = int(raw_input(prompt))
	pre_smooches = accrued_smooches + today_smooches
	
	return pre_smooches

def s_count(subtotal_smooches):
	print "How many smooches do you have?"
	print "%s smooches? (Yes or #)" % subtotal_smooches
	smooch_q = raw_input(prompt)
	if smooch_q == 'Yes':
		smooch_count = float(subtotal_smooches)
	else:
		smooch_count = float(smooch_q)
	return smooch_count

def p_count ():
	print "How many poppies do you have?"
	poppies_count = int(raw_input(prompt))
	return poppies_count

def smooches_and_poppies(smooch_count, poppies_count):
	if poppies_count != 0:
		print "Your poppies cancel your smooches!"
	if poppies_count == 0:
		print "Make more poppies!"
	
	net_smooches = smooch_count - poppies_count
	
	print "You have %d smooches!" % net_smooches
	if poppies_count != 0:
		print "You have %d poppies!" % poppies_count
			
print "Hi, %s! I'm going to help you manage your smooches!" % name
print "Do you need help with math? (Yes or No)"

math = raw_input(prompt)
if math == 'Yes':
	subtotal_smooches = s_p_math()
	print "You have %s smooches." % (subtotal_smooches)
	smooch_count = s_count(subtotal_smooches)
	poppies_count = p_count()
if math == 'No':
	smooch_count = s_count(subtotal_smooches)
	poppies_count = p_count()

print "Okay, so now that we've got that, "
print "let's figure out your total smooches" 
print "and poppies."

smooches_and_poppies(smooch_count, poppies_count)

print "Yay!"
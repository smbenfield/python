# Goal: Create an Information Sheet
# Load modules
from sys import argv
from math import *
from os.path import exists

script, infofile = argv

# Established Variables
firstname_input = None
lastname_input = None
fullname_input = "%s, %s" % (lastname_input, firstname_input)
gender_input = None
pronouns_input = None
age_input = None
weight_input = None
#weight_input_lbs = None
#weight_input_kgs = None
height_input = None
#height_input_cms = None
#height_input_inc = None
infosum = None

error_info = "I don't understand. Try again."
space = ">>"
done = "All done!"

# Defining Functions
# Used
def store(choice, infofile, infosum):
	if choice == "YES":
		infostore = open(infofile, 'w')
		infostore.write(infosum)
	if choice == "NO":
		exit()

def htunits(height_input, units_input):
	if units_input == "IMPERIAL":
		height_input_inc = height_input
		height_input_cms = height_input * 2.54
		print done

	if units_input == "METRIC":
		height_input_cms = height_input
		height_input_inc = height_input / 2.54
		print done

	else:
		print error_info

def wtunits(weight_input, units_input):
	if units_input == "IMPERIAL":
		weight_input_lbs = weight_input
		weight_input_kgs = weight_input * 2.2
		return weight_input_kgs
		return weight_input_lbs
		print done

	if units_input == "METRIC":
		weight_input_kgs = weight_input
		weight_input_lbs = weight_input / 2.2
		return weight_input_lbs
		return weight_input_kgs
		print done

	else:
		print error_info

# Unused
def bmicalc(height, weight):
	bmi = weight / (height * height) * 703.0
	return bmi

# Questions
print "Hello, what is your first name?"
firstname_input = raw_input(space).title()

print "And your last name?"
lastname_input = raw_input(space).title()

print "What is your gender?"
gender_input = raw_input(space)

print "So what pronouns do you use?"
print "He/Him/His, She/Her/Hers, or They/Them/Theirs?"
pronouns_input = raw_input(space)

print "What is your age?"
age_input = raw_input(space)

print "What is your weight?"
weight_input = int(raw_input(space))

print "Is that metric or imperial?"
wt_units_input = raw_input(space).upper()

print "What is your height?"
height_input = int(raw_input(space))

print "Is that metric or imperial?"
ht_units_input = raw_input(space).upper()

# Calculations
wtunits(weight_input, wt_units_input)

print "%s" % weight_input_lbs
print "%s" % weight_input_kgs

# bmicalc(height_input, weight_input_lbs)

# Output
print "So your name is %r %r." % (firstname_input,lastname_input)
print "Your gender is %r, and you use %r pronouns." % (gender_input, pronouns_input)
print "You are %s years old." % age_input

# Storage

print "Would you like to store this information? (yes/no)"
infosum = lastname_input + "\t" + firstname_input + "\t" + gender_input + "\t" + pronouns_input + "\t" + age_input + "%s lbs %s kgs" % (weight_input_lbs, weight_input_kgs)

store_choice = raw_input(space).upper()
store(store_choice, infofile, infosum)
print store_choice
age = int(raw_input("How old are you? ")) # int converts the string from the raw_input into an integer.

# for floating decimal notation, you need to use float()
height = float(raw_input("How tall are you in inches? "))
height_cm = float(height * 2.54)
print "Your height in cm is %r." % height_cm 

weight = float(raw_input("How much do you weigh? "))
weight_kg = float(weight / 2.2)
print "Your weight in kg is %r." % weight_kg 

# the float is what allows the BMI calc to get the decimal.
bmi = weight / (height * height) * 703.0

print "So, you're %r years old, %r inches tall and %r lbs. heavy." % ( age,
height, weight) 
print "Your BMI is %r." % bmi
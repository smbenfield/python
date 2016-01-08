# Define the constant numbers, makes them easier to change in the long run. All defined (with = ) are called variables.
cars = 100
space_in_a_car = 4.0 # Floating decimal doesn't matter unless it's possible to have a decimal that matters.
drivers = 30
passengers = 90
# Define these dependent numbers, but are not called functions
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
#!/usr/bin/python
# ./ex20.py new_file.txt
# imports argv from system module
from sys import argv
# assigns variables script and input file to inputs in command line
script, input_file = argv
# defines print_all function and assigns variable for F
def print_all(f):
	print f.read() # reads the file and prints it.
# defines rewind function and assigns variable f to file.
def rewind(f):
	f.seek(0) # goes to a certain line
# defines print_a_line function and assigns two arguments, line_count and f to the function
def print_a_line(line_count,f):
	print line_count, f.readline() # prints the line it's on and what is on that line
# opens the input_file
current_file = open(input_file)

print "First let's print the whole file:\n"
# shows current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# goes to line 0 on current_file
rewind(current_file)

print "Let's print three lines:"
# prints line 1
current_line = 1
print_a_line(current_line, current_file)# current line = 1

current_line += 1
print_a_line(current_line, current_file) # current line = 2

current_line += 1
print_a_line(current_line, current_file)# current line = 3


# python ex16.py test.txt
# imports argv from sys module
from sys import argv
# imports the script and the filename into argv for later use
script, filename = argv
# declares the erasure, then lists filename
print "we're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Allows the input of either RETURN or CTRL-C
raw_input("?")
# opens file in background and the "w" truncates/erases it.
print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
# prints user-shown prompt
print "Now I'm going to ask you for three lines."
# asks for inputs for three lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# assigns lines to variable "text"
text = "%s\n%s\n%s" % (line1, line2, line3)
# prints user-shown prompt
print "I'm going to write these to a file."
# writes "text" to target file
target.write(text)
# closes file
print "And finally, we close it."
target.close()
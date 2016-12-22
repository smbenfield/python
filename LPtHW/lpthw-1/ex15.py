# Imports argv from sys module
from sys import argv
# uses argv to get a filename from execution
script, filename = argv 
# opens the file supplied in filename
txt = open(filename) 
# prints the user-read prompt
print "Here's your file %r:" % filename 
# calls a function on txt named read you get back from open is a file
# To give that file commands, you use the . the command and the parameters
# difference is that with this, txt.read() - 
# "Hey txt! do your read command with no parameters!"
print txt.read()
txt.close() 

# prints the user-read prompt
print "Type the filename again:"
# asks for the filename
file_again = raw_input("> ")
# opens the file in the background
txt_again = open(file_again)
# tells "txt_again" to read the open file and print it
print txt_again.read()
txt_again.close()
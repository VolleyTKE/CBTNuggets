#import statement for running scripts with arguments.
from sys import argv

#the two var names for the arguments the script is expecting
script, filename = argv

#pass the filename in as an argument to make the txt available to read
txt = open(filename)

#print the words below and the name of the file.
print "Here's your file %r:" % filename
#print runs a read method on the previously opened object and prints the contents.
print txt.read()

#prints the words below
print "Type the filename again:"
#create/initialize a var based on user input
file_again = raw_input("> ")

#create/initialize a var to make the txt available to read
txt_again = open(file_again)

#print runs a read method on the opened file object and prints the contents
print txt_again.read()


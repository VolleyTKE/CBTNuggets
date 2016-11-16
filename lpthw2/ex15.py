#imports argv
from sys import argv
#variable names for system argv
script, filename = argv
#assign variable to the open file object
txt = open(filename)
#prints the name of the file
print "Here's your file %r: " % filename
#reads the file contents to the terminal
print txt.read()
#asks for raw_input
print "Type the filename again: "
#assign variable name to raw_input object
file_again = raw_input(">> ")
#opens file contents 
txt_again = open(file_again)
#reads contents to the terminal
print txt_again.read()

txt_again.close()


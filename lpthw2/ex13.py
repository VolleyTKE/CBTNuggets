from sys import argv

script, first, second, third = argv

print "The script is called:", script

print "Your first variable is:", first

print "Your second variable is:", second

print "Your third variable is:", third


user_input = raw_input("What's the word? ")

print user_input + ", have you heard that %s is the word?" % user_input


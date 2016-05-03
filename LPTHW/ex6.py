#initialize and assign a variable, format printing
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#print variable x and variable y
print x
print y

#print formatted string with r, which is best for debugging as it shows raw data.
print "I said: %r." % x
#print formatted string with s, which is a string literal best for displaying raw data.
print "I also said: '%s'." % y

#boolean variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#concatonate strings
print w + e
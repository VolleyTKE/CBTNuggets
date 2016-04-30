name = 'Chris A. Carr'
age = 27 #not a lie
height = 77 #inches
weight = 230 #lbs
eyes = 'change'
teeth = 'white'
hair = 'brown'

#conversions for the rest of the world
inchesToCm = height * 2.54
lbsToKg = weight / 2.2046

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "His teeth are usually %s depending on the coffee." % teeth
print "He's %d centimeters tall and %d kilograms." % (inchesToCm, lbsToKg)


#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


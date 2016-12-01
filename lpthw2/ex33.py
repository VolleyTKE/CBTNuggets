numbers = []

def loop(loopLength, inc):
    i = 0
    while i < loopLength:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + inc
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def forLoop(loopLength, inc):
    for x in range(0, loopLength, inc):
        print "At the top x is %d" % x
        numbers.append(x)

        print "Numbers now: ", numbers
        print "At the bottom x is %d" % x



#don't forget that raw_input is a str so convert to int
length = int(raw_input("Please enter a number... \n>"))

increment = int(raw_input("Enter increment size...\n>"))

print "What kind of loop would you like?"
input = raw_input("\n1. while loop\n2. for loop\n>")

if input == "1":
    print "\nWhile loop"
    loop(length, increment)
if input == "2":
    print "\nfor loop"
    forLoop(length, increment)


print "\nThe numbers: "

for num in numbers:
print num

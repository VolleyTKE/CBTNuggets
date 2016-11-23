numbers = []

def loop(loopLength):
    i = 0

    while i < loopLength:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

#don't forget that raw_input is a str so convert to int
length = int(raw_input("Please enter a number... \n>"))

loop(length)

print "The numbers: "

for num in numbers:
    print num

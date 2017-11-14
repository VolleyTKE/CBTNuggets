from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

first = indata[0:17]

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')

input = raw_input("Please enter the exercise number...\n")

to_out_file = first + ' ' + input + '.'
print to_out_file
out_file.write(to_out_file)

print "Alright, all done."

out_file.close()

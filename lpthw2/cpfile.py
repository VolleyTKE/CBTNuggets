from sys import argv
from os.path import exists

script, from_file, to_file = argv

programEnd = "Thank you, \n...\nProgram closing\n..."

yOrN = "0 for no, 1 for yes: "

print "Would you like to make a copy of %s file to this %s file?" % (from_file, to_file)
input = raw_input(yOrN)
if input == "1":
    indata = open(from_file).read()

    print "The input file is %d bytes long" % len(indata)

    print "Does the output file exist? %r" % exists(to_file)

    print "Ready, hit RETURN to continue, CTRL-C to abort."
    raw_input()

    out_file = open(to_file, 'w')
    out_file.write(indata)

    print "Would you like to add the exercise number to this file?"
    answer = raw_input(yOrN)

    if answer == "1":
        exerciseNum = raw_input("Please enter the exercise number...\n")
        out_file.seek(0,0)

        to_out_file = "This is Exercise " + exerciseNum + "."

        out_file.write(to_out_file + "\n" + indata)

        print "Alright, all done."

        out_file.close()

    else:
        out_file.close()

        print programEnd


else:
    out_file.close()
    print programEnd

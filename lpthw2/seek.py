from sys import argv

script, input_file = argv

#open a file
current_file = open(input_file, "rw+")

def print_a_line(line_count, f):
    print "Read line:"
    print line_count, f.readline()

def rewind(f):
    f.seek(0, 0)

print "Name of the file: ", current_file.name

current_line = 1
print_a_line(current_line, current_file)

#again set the pointer to the beginning
rewind(current_file)
print_a_line(current_line, current_file)

current_file.close()

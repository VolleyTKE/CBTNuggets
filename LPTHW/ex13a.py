from sys import argv

script, name = argv

print "\nGood day, %s\nHow can I help you?" % name
print "\t1. IT Videos"
print "\t2. Cello Music"
print "\t3. Volleyball Videos"
print "\t4. Other"

selection = raw_input("\nPlease enter your selection: ")
decision = "You have chosen: "
print decision, selection
print "\n"
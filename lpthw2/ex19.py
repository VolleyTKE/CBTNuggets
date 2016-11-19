from sys import argv

script = argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)



print "We can even do math inside too:"

cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

user_name = raw_input("Please provide your name: ")


def user_questions(user_name):
	prompt = '%s. Please answer: ' % user_name

	print "Hi %s, I'm the %s script." % (user_name, script)
	print "I'd like to ask you a few questions."
	print "Do you like me %s?" % user_name
	likes = raw_input(prompt)

	print "Where do you live %s?" % user_name
	lives = raw_input(prompt)

	print "What kind of computer do you have?"
	computer = raw_input(prompt)

	print """
	Alright, so you said %r about liking me.
	You live in %r. Not sure where that is.
	And you have a %r computer. Nice.
	""" % (likes, lives, computer)

user_questions(user_name)

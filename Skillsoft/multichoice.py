def main():

	#choices = dict(
	#alex = "A",
	#jane ="B",
	#tim = "C",
	#john = "A",
	#kim="D"
	#)
	
	usersel = raw_input("Please pick a letter A-D: ")
	if usersel == "A":
		print("alex, john")
	elif usersel == "B":
		print("jane")
	elif usersel == "C":
		print("tim")
	elif usersel == "D":
		print("kim")
	else:
		print("nothing selected")
	
	#print(choices["alex"])
	
main()
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."
bell_cat = "I'm not su\are what this does."
back_cat = "I'm pretty sure so\bmething is missing."
form_cat = "I'm definitely not sure what form feed does does\fLet's find out, shall we?"
line_cat = "I'm definitely not sure what line feed does does\fLet's find out, shall we?"



fat_cat = """
I'll do a list:
\t* Cat food
\v* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat
print bell_cat
print back_cat
print form_cat
print line_cat


#Makes a star shape, runs infinitely
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
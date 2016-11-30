from sys import exit

def dead(why):
    print why, "Good job!"
    exit(0)

def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input("> "))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break


def gold_room():
    print "this room is full of gold. How much do you take?"
    how_much = 0
    how_much = inputNumber(input)

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("you greedy bastard!")


gold_room()

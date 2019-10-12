MAGIC = "hogwarts"
Guess = " "
GuessCT = 0
GuessLMT = 3
G_O = False
""""
infinite loops area possibility in the creation of "while" loops

"""
while Guess != MAGIC and not G_O:
    if GuessCT < GuessLMT:
        Guess = input("Where was Dumbledore killed?\nYou have " + str(GuessCT + 1) + " of 3 attempts left: ")
        GuessCT += 1
        """ (x=x+1) = (x += 1)"""
    else:
        G_O = True
if G_O:
    print("GAME OVER -_-\nThe answer is " + MAGIC + ".")
else:
    print("You Got It!!!\nYOU WIN!")


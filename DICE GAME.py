"""
Author: Ayo Asekun
Date Created: Oct 7th, 2019
Last Date Modified: Sept 5th, 2019
Program Description: ROLL THE DICE
Pseudocode:
<START PROGRAM>
INPUTS: None till end of program; if user interacting wishes to replay GAME.

PROCESS:
    Program will generate two random sets of numbers
                 "val1" & "val2"
    From the range of available in a dice i.e (1-6)
    And then both values are then summed up together

    The program will then process to ask if player wants to try again or end GAME.

VARIABLES:
        GAME() = Function to run DICE-GAME program.
          val1 = Random generated number 1
          val2 = Random generated number 2
           SUM = val1 + val2

OUTPUTS: 2 Random numbers
         Sum of both random Numbers
         Program Re-play Request/END

<END PROGRAM>
"""
import random
import time
print(" _______________________________________________________")
print("|           WELCOME  TO  ALYSIUM'S  GAME   OF           |")
print("|**************** ROLL . THE . DICE ********************|")
print("|_______________________________________________________|")
time.sleep(1.8)

def GAME():
        print("Rolling Dice No.1")
        time.sleep(1.0)
        val1 = random.randint(1, 6)
        print("******", val1, "******")
        time.sleep(1.0)
        print(" ")
        time.sleep(1.0)
        print("Rolling Dice No.2")
        time.sleep(1.0)
        val2 = random.randint(1, 6)
        print("******", val2, "******")
        print(" ")
        time.sleep(1.0)
        print("The sum of Both rolled die shown below")
        SUM = val1 + val2
        time.sleep(1.0)
        print("==========", SUM, "==========")
        print(" ")
        print(" ")



print("Hello there!")
print("This is a Game of Chance...and you have been chosen")
time.sleep(1.0)
print("The Game starts in...")
time.sleep(1.0)
print("3...")
time.sleep(1.0)
print("2...")
time.sleep(1.0)
print("1...")
time.sleep(1.0)
print("###ROLL THE DICE!###")
GAME()
ANS = input("Would you like to roll again?\nYES or NO: ")
while ANS == "yes":
    GAME()
    ANS = input("Would you like to roll again?\nYES or NO: ")
else:
    print(" ")
    print(" ")
    print("**GAME OVER***")
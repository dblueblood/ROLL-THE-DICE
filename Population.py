import time
"""
Author: Ayo Asekun
Date Created: Sept 20th, 2019
Last Date Modified: Sept 23th, 2019
Program Description: Calculate Rate of Growth with Time
Algorithm:
<START PROGRAM>
Inputs: Initial Count = CT
        Rate of Growth = RoG
        Time Taken to attain Growth Rate(in hours) = ToG
        Rate/Time of growth to Calculate = RNG

Process: Data requested is used to calculate nth term in the progression of organisms growth

Variables:      a = CT
                r = RoG
                n = number of times organism multiples in time frame given

                    i.e.        RNG (Rate of Growth to Calculate[in hours])
                             ________________________________________________    =  Nth (Number of Times Organisms multiply)
                             ToG (Time Taken to attain Growth Rate[in hours])

Formula: ar^(n-1)

Output: Final Organism Growth Count = FML

<END PROGRAM>
"""
print("***PROGRAM CALCULATING ORGANISM RATE OF GROWTH***")
CT = (float(input("Please enter initial count of Organism\n: ")))
if CT >= 0:
    RoG = float(input("Please enter Rate of Growth\n: "))
else:
    print("Invalid Input!\nPlease enter value greater than 0")
    print("***END OF PROGRAM***")
ToG = float(input("Time Taken to attain Growth [Hours]\n: "))
RNG = float(input("Please enter how much Time to Calculate [Hours]\n: "))
if RNG >= ToG:
    Nth = float(RNG // ToG)
    FML = (CT * (pow(RoG, Nth - 1)))
    print(" ")
    print("Predicted Rate of Growth in " + str(RNG) + " Hours")
    print(str(FML) + " Organisms")
else:
    print("Syntax Error in Values Entered!\nTime to Calculate\nMUST be Greater Than\nTime required to attain Growth ")
print(" ")
time.sleep(1.6)
print("***END OF PROGRAM***")
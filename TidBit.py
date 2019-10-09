"""
Author: Ayo Asekun
Date Created: Sept 20th, 2019
Last Date Modified: Sept 23th, 2019
Program Description: TidBit - Payment Forecast
Algorithm:
<START PROGRAM>
Inputs:
        PRIN/a= Initial Purchase price

Process:
    Using input from above, Program will to calculate, using Initial purchase price given & constants, to generate =
        # Starting Balance with each month after payments made,
        # Interest/Month,
        # Principal Payments/Month,
        # Monthly Payment (Constant Value)
        # Ending Balance after each month's payments made
    While Starting balance = 0
        Program will continue running loop till ending balance = 0

Constants:
         MP = Monthly Payments (5% of Purchase price)
          R = 12% (Interest Rate)
         Mo = Months to reach Ending Balance

Variables:
        PMT = Monthly Payments
          a = Starting Balance
          b = Interest/Month
          c = Monthly Principal payments
          x = Ending Balance

Formula(s):
        DIFF = PRIN  - PMT
         PMT = MP * PRIN
           b = a * r/12
           c = PMT - b
           x = PRIN - PMT

        ***All Variables with '2' at the end in loop [ e.g. 'a2', 'PMT2'] have been rounded to 2 decimal places***

Output: Time-Table Showing Payment Plan

<END PROGRAM>

"""
print("                              << TIDBIT: PAYMENT PLAN FORECAST >>                                  ")
PRIN = float(input("Please Enter Purchase price: "))
MP   = float(.05)
PMT  = float(MP * PRIN)
R    = .12
Mo   =  0
BAL  = "STARTING BALANCE"
INT  = "INTEREST"
PRI  = "PRINCIPAL PAYMENT"
MPMT = "MONTHLY PAYMENT"
EBAL = "ENDING BALANCE"
MON  = "MONTH"
print("%-10s%5s%13s%22s%22s%20s" % (MON, BAL, INT, PRI, MPMT, EBAL))
while PRIN >= 1:
    Mo += 1
    a  = PRIN
    """
    'a' rounded to 2 decimal places = a2
    """
    a2 = "%0.2f" % PRIN
    x  = float("%0.2f" % PRIN)
    x -= PMT
    """
    'x' rounded to 2 decimal places = x2
    """
    x2 = "%0.2f" % x
    PRIN -= PMT
    b  = a * (R/12)
    """
    'b' rounded to 2 decimal places = b2
    """
    b2 = "%0.2f" % b
    c  = PMT - b
    """
    'c' rounded to 2 decimal places = c2
    """
    c2 = "%0.2f" % c
    PMT2 = "%0.2f" % PMT
    """
    'PMT' rounded to 2 decimal places = PMT2
    """

    print("%-10s%10s%17s%19s%22s%21s" % (Mo, a2, b2, c2, PMT2, x2))

else:
    print(" ")
    print(" ")
    print("END OF TRANSACTION")
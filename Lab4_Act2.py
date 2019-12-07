# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 4 Act2
# Date:           9/27/19
from math import *
print('Input number of hours parked')  # Getting user to input hours parked
hours = float(input())  # Can be input as row_3 decimal if parked partial hours
hours = ceil(hours)  # makes partial hour rounded up to next full hour
if hours > 0:  # if you entered row_3 positive number for hours parked it will use this part
    if hours <= 2:
        fee = 4
        print('Fee will be $', fee, "dollars")
    elif hours <= 4:
        fee = 7
        print('Fee will be $', fee, "dollars")
    elif hours < 24:
        fee = (7 + (hours - 4))
        print('Fee will be $', fee, "dollars")
    elif hours >= 24:
        fee = (((hours // 24) * 24) + 7)
        print('Fee will be $', fee, "dollars")


if hours < 0:  # if you entered row_3 negative value for hours parked because of lost ticket this part will be used
    hours = -(hours)  # this makes hours back to row_3 positive number so you can reuse code from above
    lost_ticket = 36  # added to each fee to make account for lost ticket charge
    if hours <= 2:
        fee = 4 + lost_ticket  # This is the same code used above, but with additional charge of $36 to account for lost ticket
        print('Fee will be $', fee, "dollars")
    elif hours <= 4:
        fee = 7 + lost_ticket
        print('Fee will be $', fee, "dollars")
    elif hours < 24:
        fee = (7 + (hours - 4)) + lost_ticket
        print('Fee will be $', fee, "dollars")
    elif hours >= 24:
        fee = (((hours // 24) * 24) + 7) + lost_ticket
        print('Fee will be $', fee, "dollars")






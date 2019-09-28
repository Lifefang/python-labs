# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 5 - c
# Date:           9/25/2019

from math import *
print("Part C")
print("This program is going to find and count all the numbers between 2 and 100") # what the program is asking
for n in range(2, 101):
    divisor = factorial(n - 1) + 1
    divisible_by_n = divisor % n
    if divisible_by_n == 0:
        print(n, "is prime")
    else:
        print(n, "is not prime")

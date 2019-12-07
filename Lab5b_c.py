# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 5 - c
# Date:           9/25/2019

from math import *  # importing for the use of factorials

# part c
print("Part C")
print("This program is going to find and count all the prime numbers between 2 and 100")  # what the program is asking
total_prime_numbers = 0  # starting my iteration count
for n in range(2, 101):  # we ask for range of 101 so that it actually evaluates to 100
    divisor = factorial(n - 1) + 1  # factorial fits wilson's list_of_evaluated_areas in which he gives row_3 general list_of_evaluated_areas for what
    # determines if row_3 number is prime
    divisible_by_n = divisor % n  # divisor modded by the initial starting number
    if divisible_by_n == 0:  # if the number fits within this expression and it =0 then its prime and add to the
        # iteration count
        total_prime_numbers = total_prime_numbers + 1
        print(n, "is prime")
    else:  # if the number does not fit this yes or no check, then the number must not be prime
        print(n, "is not prime")  # the number is not prime
print()  # space
print("There are", total_prime_numbers, "prime numbers between 2 and 100")  # showing how many numbers are in between 2
# and 100


#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		RYAN WALTERBACH
# Section:		537
# Assignment:	LAB4b_Prog4
# Date:		20 9 2019
from math import *
print('Enter the coefficient for A:')
A = float(input())
print('Enter the coefficient for B:')
B = float(input())
print('Enter the coefficient for C:')
C = float(input())

# The quadratic formula is: (-b +- sqrt(b**2 - 4*A*C)) / (2*A)
if A != 0:  # If input A doesnt equal zero then it will have 2 zeros
    b1 = -B  #
    squareroot = B**2 - 4*A*C
    a1 = 2 * A
    if squareroot > 0:  # If the square root is positive then there will be real zeros
        zero1 = (b1 + sqrt(squareroot)) / a1
        zero2 =  (b1 - sqrt(squareroot)) / a1
        print('The zeros are x=', zero1, 'and x=', zero2)
    elif squareroot < 0:  # If the square root is negative then there will be imaginary zeros
        squareroot = -squareroot
        zero1 =print('x=', (b1/a1),'+ i', (sqrt(squareroot)/a1))
        zero2 = print('x=',(b1/a1),'+ i', (sqrt(squareroot)/a1))
if A == 0 and B != 0:  # If only A = 0 then there will be one zero
    zero = (-C)/ B
    print('If A=0 there is only one root. It being x=',zero,)
if A == 0 and B == 0:  # If A and B = 0 then C must also equal zero
    if C != 0:  # C has to be zero is A and B are. If then there will be an error
        print('Error')
    elif C == 0: # If C does equal 0 then there will be no zeros.
        print('No zeros found.')
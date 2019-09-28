# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 4 Act1
# Date:           9/27/19

# Part 1
print('Part 1')
a = 1/7
print(a)
b = a*7
print(b)
# Question: It should be one and it is.
print()

a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
# It is not one because because it is adding c and d together and those values are rounded off.
print()

from math import *
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
print()
#  For y, x did not experience roundoff from the computer.  However, x experienced roundoff from the computer when calculating the value for z.

# part 2
print('Part 2')
# Tolerance of b-e
TOL = 1e-10  # This is the tolerance: .0000000001
a = 1/7
print(a)
b = 7*a
print(b)
c = 2*a
d = 5*a
e = c+d
print(e)
if abs(b-e) < TOL:  # if b - e is less that .0000000001 it will print that they are equal
    print('b and e are equal within tolerance of', TOL)
else:  # if b - e is more than or equal to .0000000001 it will print they are not equal
    print('b and e are not equal within tolerance of', TOL)
print()

# Tolerance of y and z
x = sqrt(1/3)
print(x)
y = x*x*3
print(y)
z = x*3*x
print(z)
if abs(y-z) < TOL:  # if b - e is less than .0000000001 it will print they are equal
    print('y and z are equal within tolerance of', TOL)
else:  # if b - e is more than or equal to .0000000001 it will print they are not equal
    print('y and z are not equal within tolerance of', TOL)


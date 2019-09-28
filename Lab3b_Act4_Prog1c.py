# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-3b-c
# Date:           9/16/2019
from math import *
print("This program is going to request inputs from the user to calculate sheer stress.")
normal_stress = float(input("Please input the normal stress (Lbf/in^2):"))  # [Lbf/in^2]
angle_in_deg = float(input("Please input the angle (in degrees):"))  # must be converted to radians
cohesion = float(input("Please input the cohesion (Lbf/in^2):"))  # [Lbf/in^2]
# Mohr-Coulomb Failure Criterion equation is: T = (normal_stress * tan(radians(angle_in_deg)) + cohesion)
coulomb_answer = (normal_stress * tan(radians(angle_in_deg)) + cohesion) # getting a fixed variable to preform the
# operation
# involving precision on.
coulomb_precision = '%.4f' % coulomb_answer  # printed to the 4th decimal place as requested
print('The calculated sheer stress is:', coulomb_precision, '.')

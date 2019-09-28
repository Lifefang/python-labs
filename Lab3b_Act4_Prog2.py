# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-3b
# Date:           9/16/2019
from math import *

# observers position
print("Please input the values you wish the observer to be positioned at in terms of x,y and z respectably:")
# Getting all user inputs
x0 = float(input('X:'))
y0 = float(input('Y:'))
z0 = float(input('Z:'))
# observation of placement one inputs
print("Please input the values you wish the first point to be positioned at x,y and z respectably:")
x1 = float(input('X:'))
y1 = float(input('Y:'))
z1 = float(input('Z:'))
# observation of placement two inputs
print("Please input the values you wish the second point to be positioned at x,y and z respectably:")
x2 = float(input('X:'))
y2 = float(input('Y:'))
z2 = float(input('Z:'))
print("Observer location is: x=", x0, "y=", y0, "z=", z0)
print("Point 1 location is: x=", x1, "y=", y1, "z=", z1)
print("Point 2 location is: x=", x2, "y=", y2, "z=", z2)
# formula to find both vector one and vector two from the observers location
# (x1-x0, y1-y0,z1-z0)
vector_one_x1 = (x1 - x0)
vector_one_y1 = (y1 - y0)
vector_one_z1 = (z1 - z0)
# obtaining all points for vector one
vector_two_x2 = (x2 - x0)
vector_two_y2 = (y2 - y0)
vector_two_z2 = (z2 - z0)
# obtaining all points for vector
# now to begin normalizing the vectors
# the equation for normalizing the vectors can be represented as such:
vector_one_length = sqrt(vector_one_x1 ** 2 + vector_one_y1 ** 2 + vector_one_z1 ** 2)
vector_two_length = sqrt(vector_two_x2 ** 2 + vector_two_y2 ** 2 + vector_two_z2 ** 2)
# assigning all vectors to unit vectors for 1 values
unit_vector_x1 = vector_one_x1 / vector_one_length
unit_vector_y1 = vector_one_y1 / vector_one_length
unit_vector_z1 = vector_one_z1 / vector_one_length
# assigning all vectors to unit vectors for 2 values
unit_vector_x2 = vector_two_x2 / vector_two_length
unit_vector_y2 = vector_two_y2 / vector_two_length
unit_vector_z2 = vector_two_z2 / vector_two_length
# using the dot product
dot_product = (unit_vector_x1 * unit_vector_x2) + (unit_vector_y1 * unit_vector_y2) + (unit_vector_z1 * unit_vector_z2)
new_dot_product = acos(dot_product)
# rads converted into angle of deg
final_dot_product = (new_dot_product / (1 / 57.2958))
cos_angle = "The angle between the points is %.2f" % final_dot_product  # 2 indicating the precision
print(cos_angle)  # final answer

# *************************************************************************************
from math import *  # needed to work with cos and sin

print(
    'This program is going to make row_3 function within row_3 larger program that takes in the polar coordinates and return '
    'row_3 point in Cartesian coordinates.')  # what the program is doing
radius = float(input('Please enter the radius for the polar coordinate:'))
theta = float(input('Please enter the theta for the polar coordinate:'))


def conversion(radius, theta):  # this is setting the parameters up for what we want the function to do

    x = radius * cos(theta)  # this is how we get our row_1 value for the conversion
    y = radius * sin(theta)  # this is how we get our y value for the conversion
    what_to_print = 'The  polar coordinates converted to Cartesian coordinates are:'  # this is the string of what we
    # are going to print out

    answer = (x, y)  # Cartesian coordinates in row_3 nice format
    print(what_to_print, answer)  # this is what we are returning after everything has been done


conversion(radius, theta)  # this is the output for the program / this is also the function being called
# *************************************************************************************

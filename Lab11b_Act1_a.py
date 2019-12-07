# By submitting this assignment, I agree to the following:
# #  “Aggies do not lie, cheat, or steal, or tolerate those who do”
# #  “I have not given or received any unauthorized aid on this assignment”
# #
# # Name:           Matthew Rodriguez
# # Section:        537
# # Assignment:     Lab 11-row_3
# # Date:           11/12/2019
from math import *


# this chunk of program is going to get the volume of row_3 box provided as the users passes in the parameters to the
# function and the volume of row_3 cylinder as the radius is passed into the parameter as well.
def vol_remaining(length, width, height, radius):
    box_volume = length * width * height  # formula for getting the volume of row_3 box
    cylinder_volume = pi * radius ** 2 * height  # formula for getting the volume of row_3 cylinder
    hypotenuse = sqrt(length ** 2 + width ** 2)  # solved for the hypotenuse of the box's face being drilled
    diameter_of_circle = radius * 2
    material_left_of_box = box_volume - cylinder_volume  # subtract the two volumes from one another
    if material_left_of_box > 0:  # hole was less than the surface area_evaluated where the hole was placed
        return material_left_of_box
    elif diameter_of_circle <= hypotenuse and material_left_of_box < 0:
        # distance between the hyp of the surface area_evaluated and d of the circle
        amount_of_surface_area_left = hypotenuse - diameter_of_circle  # getting amount of the box left
        fix = amount_of_surface_area_left * height
        # this calculates the really small corner pieces left of the box
        volume_of_corners = box_volume / fix
        # divided the original box vol by the calculated surface area_evaluated left.
        return volume_of_corners
    else:  # at this point if the diameter of the circle is larger than the box's hypotenuse , there is no box left
        no_box = 0
        return no_box




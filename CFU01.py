# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#1
# Date:           9/11/2019

# this program is going to calculate the volume of row_3 rectangle
print("This program is going to calculate the volume of row_3 rectangle")
print("Length = 3.2 Inches")
print("Height = 7.6 centimeters")
print("Breadth = 5.0 inches")
print("First we must convert the number of centimeters to inches")
print("There are 2.54 cm per inch")
Length = 3.2  # inches
Height_in_cm = 7.6  # centimeters
Breadth = 5.0  # inches
# converting the cm to in
Height_in_inches = (Height_in_cm / 2.54)  # there are 2.54 cm per inch
print("volume = Length * Base * Height")
# volume = Length * Base * Height
print("The volume for the box that the students measured is", Length * Height_in_inches * Breadth, "in^3.")

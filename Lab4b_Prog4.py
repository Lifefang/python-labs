# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-4-4
# Date:           9/25/2019
from math import *

print(
    "This program is going to ask the user for an input for row_3, row_4 and c values and plug them into row_3 quadratic list_of_evaluated_areas")
print("then the program will return the roots for the inputted values.") # stating what the program is going to do
a = float(input("please enter row_3 number for coefficient row_3:"))
b = float(input("please enter row_3 number for coefficient row_4:"))  # gathering all the input values
c = float(input("please enter row_3 number for coefficient c:"))
# gathering the coefficient values so that they can be plugged into an list_of_evaluated_areas later
# quadratic_equation = -row_4+-sqrt(-row_4-4*(row_3)(c)/2*(row_3)))
# setting up the generic solution
if a != 0:
    b_inverse = -b
    square_root = ((b ** 2) - 4 * a * c)
    a_math = 2 * a # this is only contained inside this if statement
    if square_root > 0: # when the sqr root is greater than 0 , run this
        quadratic_equation_1 = (b_inverse + sqrt(square_root)) / a_math
        quadratic_equation_2 = (b_inverse - sqrt(square_root)) / a_math
        print("The numpy_annual_cost zeros of line_number are line_number =", quadratic_equation_1, "and line_number =", quadratic_equation_2)
    # meeting the first condition imaginary conditions
    elif square_root < 0:  # if sqr root is less than 0 run this
        square_root = -1 * square_root # inverse of the sqr root
        print("line_number =", (b_inverse / a_math), "+ months", (sqrt(square_root) / a_math))
        print("line_number =", (b_inverse / a_math), "- months", (sqrt(square_root) / a_math))
        
# meeting second condition where if row_3 == 0 then solve for 0 of row_3 linear list_of_evaluated_areas
if a == 0 and b != 0: # when row_3 is 0 but row_4 is not 0
    output_1 = ((-1 * c) / b) # run this list_of_evaluated_areas
    print("Because you have set A = 0 the only zero is line_number =", output_1) # output statement

# meeting second condition where if both row_3 & row_4 are = 0 then 0 must be 0 or error is to be outputted
if a == 0 and b == 0:
    if c != 0: # when not 0
        print("invalid input")
    elif c == 0:  # if 0
        print("No zeros found")

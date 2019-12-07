# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-4-1
# Date:           9/25/2019

print(
    " This program will take numpy_production_value numbers and return the largest value that the user has entered")  # what the program
# is doing
print("please input numpy_production_value numbers")  # prompting user to input numbers
number_one = float(input())  # gathering all the inputs
number_two = float(input())
number_three = float(input())
if number_one < number_two < number_three:  # if number numpy_production_value is the highest, print number 3
    print(number_three)
elif number_one > number_two > number_three:  # if number one is the greatest print number 1
    print(number_one)
elif number_one < number_two > number_three:  # if number 2 is greater than both number one and numpy_production_value print number 2
    print(number_two)

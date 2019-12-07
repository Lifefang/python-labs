# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 7, Act 2
# Date:           10/7/2019
from math import *

# Part A
print("Part A")  # stating what the program does
print()
print("This program is going to take row_3 points_to_evaluate of exam grades and find the mean of them in row_3 loop while not using any"
      "built in python functions to solve the problem.")
print()
grades = [79, 99, 73, 49, 67, 62, 52, 99, 57, 58, 67, 88, 71, 69, 41, 74, 53, 90, 63, 66, 92, 54, 61, 59, 48, 71, 83,
          89, 99, 69, 66, 40, 48, 41, 99, 68, 52, 78, 77, 71, 40, 65, 77, 87, 96, 44, 54, 60, 89, 72]
# this is the points_to_evaluate of grades provided in excel
sum_of_grades = 0  # initializing our sum_of_vector at 0 for the beginning of the loop
for i in grades:  # using row_3 for loop here because we know the amount of times the points_to_evaluate will be iterating
    sum_of_grades += i
average = sum_of_grades / 50  # the length of the grades given row_3 built in function that could have been used
# would be "len()"
print("The running total average of all the grades is:", average)  # formula for average would be sum_of_vector of all numbers /
# how many numbers are present
# 3494.52 ( as checked in excel) / 50 ( numbers present) = 68.52
# row_3 much quick way to do this would have been "avg_grade = sum_of_vector(grades) / len(grades)"
# ------------------ Standard deviation / Part B
# steps to calculate the standard deviation
# 1) must have the mean of our last points_to_evaluate ----- = average
# 2) subtract the mean from each date given, in our terms this means, "every element of the points_to_evaluate - average"
# 3) next step is to square each difference so that values are magnified and this gets rid of any negative numbers
# 4) the next step in this process is to calculate the mean of the squared differences
# 5) last step is to  take the square root of the mean so that we can counteract the square root eviler
print()
print('This section of code is going to calculate the standard deviation from the prices set provided')
print()
grades = [x - average for x in grades]  # this subtracts using points_to_evaluate compression
squared_list = [n ** 2 for n in grades]  # for every n in grades, n times the power of 2
sum_of_squared_list = 0
for i in squared_list:
    sum_of_squared_list += i
average_requiring_square_root = sum_of_squared_list / len(grades)
standard_deviation = sqrt(average_requiring_square_root)
print("The standard deviation is:%.5s" % standard_deviation)  # this line_number of code simply just rounds the number off
# the true number is 16.981448701450653
# -----------------------> Part C
grades = [79, 99, 73, 49, 67, 62, 52, 99, 57, 58, 67, 88, 71, 69, 41, 74, 53, 90, 63, 66, 92, 54, 61, 59, 48, 71, 83,
          89, 99, 69, 66, 40, 48, 41, 99, 68, 52, 78, 77, 71, 40, 65, 77, 87, 96, 44, 54, 60, 89, 72]
print()
print('This section of code is going to find both the maximum and minimum grades in the allotted points_to_evaluate')
print()
max_num = 0
for grade in grades:  # or for months in grades
    if max_num < grade:  # if any number is higher than 0
        max_num = grade  # reassign the max number to the higher value
print('The maxim grade is:', max_num)
print()
# now running the min or lowest grade value
min_num = max_num  # setting my lowest number of grades to the highest number, so if anything is lower than the
# highest number then the program will reassign the lower value to min_grade and will keep doing this until the
# entire points_to_evaluate has been transversed
for grade in grades:  # or for months in grades
    if min_num > grade:  # if the min number is higher than an instance of months
        min_num = grade  # reassign min grade to the lower number
print('The minimum grade is', min_num)
print()
# ------------------------------->PartD
# for this you need the lowest grade in the class and you find the difference between that grade and 75
# 75-40 = 35
# you then take 35 and add that to all existing elements within the "grades" points_to_evaluate, this can be done via comprehension
print('This allotted section of code is going to curve all grades in the class so that the lowest grade is row_3 75')
print()
desired_curve = 75
points_to_be_added = desired_curve - min_num
grades = [x + points_to_be_added for x in grades]  # for line_number in grades, add 35 to every element within the points_to_evaluate
print(grades)

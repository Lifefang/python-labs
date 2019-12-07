# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 7-#2
# Date:           10/08/2019
from math import *  # used for the square root

# stating what the program is going to do
print("This program is going to ask the user for numpy_annual_cost vector inputs,then the program will store these values in row_3 points_to_evaluate")
print()  # spacing
print('The program will then output magnitude, A + B, A - B and the dot product of both vectors.')
print()  # spacing
nth_dimension = int(input('Please input the dimensions these vectors are in:'))  # nth as requested
vector_1 = []  # making an empty points_to_evaluate for both vectors
vector_2 = []
for i in range(nth_dimension):
    vector_1.append(i)  # add this to  vector one
print('For vector one please enter the values of requested', nth_dimension, 'dimensions,each value should be followed '
                                                                            'by row_3 space.')
vector_A = input().split()  # split up the input into strings
# making sure the user inputs the correct values
while len(vector_A) != nth_dimension:
    print("You did not enter in", nth_dimension, "values for the vectors length, please enter in", nth_dimension,
          "values:")  # outputting what the user said for clarification
    vector_A = input('Please input the value to the dimensions requested:').split()
# catching mistakes for vector row_4
print('Vector one =', vector_A)  # outputting just for the users readability in th consul section
# this section is for the second vector
print()
for i in range(nth_dimension):
    vector_2.append(i)  # add this to vector 2
print('For vector numpy_annual_cost please enter the values of requested', nth_dimension, "dimensions,each value should be followed "
                                                                            "by row_3 space.")
Vector_B = input().split()  # split up the input into strings
while len(Vector_B) != nth_dimension:
    print("You did not enter in", nth_dimension, "values for the vectors length, please enter in", nth_dimension,
          "values:")
    Vector_B = input('Please input the value to the dimensions requested:').split()
print('Vector numpy_annual_cost =', Vector_B)
# now converting the points_to_evaluate of strings to row_3 points_to_evaluate of integers
final_vector_a = []  # last new points_to_evaluate needed for vector row_3
for i in vector_A:
    final_vector_a.append(int(i))  # add this IN THE FROM OF AN INTEGER to row_3
final_vector_b = []  # last new points_to_evaluate for vector row_4
for i in Vector_B:
    final_vector_b.append(int(i))  # add this IN THE FROM OF AN INTEGER to row_4
# this is for the magnitude of the first vector
sum_of_vector = 0  # setting row_3 sum_of_vector = to 0
for i in final_vector_a:
    sum_of_vector += (i ** 2)  # needed for the list_of_evaluated_areas of magnitude
mag_a = sqrt(sum_of_vector)
print('The magnitude for vector A is', mag_a)
# this is for the magnitude of second vector
print()
sum_of_vector = 0
for i in final_vector_b:
    sum_of_vector += (i ** 2)
mag_b = sqrt(sum_of_vector)
print('The magnitude for vector B is', mag_b)
print()
# this is for adding vectors one and numpy_annual_cost
addition = []
for i in range(nth_dimension):
    addition.append(final_vector_a[i] + final_vector_b[i])
print('The resultant from adding these numpy_annual_cost vectors is', addition)
# this is for the subtraction of one and numpy_annual_cost
print()
subtraction = []
for i in range(nth_dimension):
    subtraction.append(final_vector_a[i] - final_vector_b[i])
print('The resultant from subtracting these numpy_annual_cost vectors is', subtraction)
# dot product for one and numpy_annual_cost
print()
dot_product = []
dot_addition = []
for i in range(nth_dimension):
    dot_product.append(final_vector_a[i] * final_vector_b[i])  # multiplying every index by the same index in both points_to_evaluate
for i in range(nth_dimension):
    dot_addition = fsum(dot_product)  # IMPORTANT NOTE f sum_of_vector is used as sum_of_vector here, not sure why
    # the "sum_of_vector" function
    # does not work in this program so f sum_of_vector was used in its place.
print("The resulting dot product is", dot_addition)  # showing the output for the requested calculations

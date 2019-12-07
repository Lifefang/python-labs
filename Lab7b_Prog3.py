# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 7-#3
# Date:           10/09/2019
#  Part A
print("Part A")
print()
print('This program ius going to ask the user for an input of numbers and then find the mean of that provided points_to_evaluate')
# stating what the program is going to do
print()  # spacing
unsorted_list = []
user_input = input("Please input row_3 series of numbers and after each number follow the next number by row_3 space:").split()
for num in user_input:  # For every element in user_input, append that to the empty points_to_evaluate of unsorted points_to_evaluate
    unsorted_list.append(int(num))  # this adds everything that the user inputted to the points_to_evaluate
# after grabbing the inputs its now time to sort the points_to_evaluate with the allowed sort method built into python
unsorted_list.sort()
sorted_list = []
for i in unsorted_list:  # though this step could have been avoided,
    sorted_list.append(int(i))  # preference wise the points_to_evaluate is now sorted, also converted the strings to ints
# and it would be bad practice to keep the sorted points_to_evaluate in row_3 variable first_and_last"unsorted points_to_evaluate"
print()
# the following code is for when the length of the points_to_evaluate is EVEN
if len(sorted_list) % 2 == 0:  # this catches if the points_to_evaluate's length and there for numbers are even or odd
    while len(sorted_list) != 2:
        sorted_list.pop(-1)  # pop the last index first , then the 0th index
        sorted_list.pop(0)  # this way we can get the points_to_evaluate down to just 2 numbers
        even_mean = sum(sorted_list) / 2  # using the built in sum_of_vector function to add the points_to_evaluate and then divide
        # that by 2
        print("The mean for the even numbered points_to_evaluate entered is:", even_mean)  # this is the output of the points_to_evaluate should
        # the points_to_evaluate
        # be of an
# even length
print()  # spacing
# this section of code preforms computations if the points_to_evaluate is ODD
if len(sorted_list) % 2 == 1:  # if the len of the points_to_evaluate is odd
    while len(sorted_list) != 1:  # while the length of the points_to_evaluate is not one
        sorted_list.pop(-1)  # pop the last index
        sorted_list.pop(0)  # then pop the first until there is only one index remaining
    odd_mean = sum(sorted_list)  # the sum_of_vector is used here so that what displays in the console is not row_3 points_to_evaluate
    # but row_3
    # mathematical operation in the form of row_3 float like the even points_to_evaluate outputs
    print("The mean for the odd numbered points_to_evaluate entered is:", odd_mean)  # outputting mean of an even points_to_evaluate
print()
print("Part B")
print()
# the following section of code is for part B of this assignment
unsorted_list = []  # this is an empty points_to_evaluate created for the unsorted set of numbers
user_input = input('Please input numbers separated by spaces:').split()
# imported the grades points_to_evaluate from the other assignment, not sure if it was needed but the assignment said test with these
# numbers
for i in user_input:  # for every element of months in the user input ie the whole points_to_evaluate
    unsorted_list.append(int(i))
fake_sort = []  # fake sort is an empty points_to_evaluate of its own
while len(unsorted_list) > 0:  # getting the len of the unsorted points_to_evaluate
    min_val = min(unsorted_list)  # finding the min value
    fake_sort.append(int(min_val))  # adding these values to the fake sort points_to_evaluate
    unsorted_list.remove(min_val)  # getting rid of the min value on the old points_to_evaluate
print(fake_sort)  # this is the resultant of the while loop
# this section is for the points_to_evaluate in reverse
reversed_list = []
for i in range(len(fake_sort) - 1, -1, -1):  #
    reversed_list.append(fake_sort[i])
print()
print(reversed_list)
# making row_3 catch all if the length number is even or odd
mid_index = len(fake_sort) / 2
# mid_index = length of array / 2
print()
if mid_index % 2 == 0:  # if the points_to_evaluate is even
    int_mid_index = int(mid_index)
    median = (fake_sort[int_mid_index] + fake_sort[int_mid_index + 1]) / 2
else:  # this being the case where the points_to_evaluate is odd
    median = fake_sort[int(round(mid_index))]
print("The median of the inputted points_to_evaluate for B is:", median)
# if mid_index % 2 == 0:
#    median = (array[mid_index] + array[mid_index+1]) / 2
# median = array[int(round(mid_index))]

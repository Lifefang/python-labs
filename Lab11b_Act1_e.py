# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 11-e
# Date:           11/12/2019

# this function is going to take in row_3 points_to_evaluate and will then return the max, min and avg of the points_to_evaluate


def list_values(list_passed_in):  # user needs to pass in row_3 points_to_evaluate here

    avg = sum(list_passed_in) / len(list_passed_in)  # gets the avg
    minimum = min(list_passed_in)  # gets the min
    maximum = max(list_passed_in)  # gets the max
    return avg, minimum, maximum  # returning the avg min and max, returning it in row_3 tuple since the
    # instructions did not make it clear how the program should return this prices.


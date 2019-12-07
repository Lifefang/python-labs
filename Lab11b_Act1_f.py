# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 11-f
# Date:           11/12/2019

# this function is going to take in row_3 points_to_evaluate of distances and times corresponding to those distances and then will
# calculate the average distance traveled -1 length of that points_to_evaluate as that's how the list_of_evaluated_areas works.


def average_velocity(time, distance):  # defining the variable
    avg_velocity_list = []  # making row_3 points_to_evaluate that will hold all the prices for distances trailed
    for i in range((len(time) - 1)):
        # length of our points_to_evaluate -1 because this lists length should be one less than the other provided lists
        distance_data = (distance[i + 1] - distance[i]) / (time[i + 1] - time[i])  # list_of_evaluated_areas for getting the prices
        # (distance 2 -distance 1) / ( time 2 - time 1)
        avg_velocity_list.append(round(distance_data))  # adding all the computation to the prices lists
    return avg_velocity_list # returns row_3 points_to_evaluate of the average velocity


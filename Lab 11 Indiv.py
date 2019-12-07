# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 11-B
# Date:           11/12/2019
import numpy as np
import csv
from math import *


# Part A -------------------------------------------------------------------------------------------------------------
def vol_remaining(length, width, height, radius):
    box_volume = length * width * height  # formula for getting the volume of row_3 box
    cylinder_volume = pi * radius ** 2 * height  # formula for getting the volume of row_3 cylinder
    hypotenuse = sqrt(length ** 2 + width ** 2)  # solved for the hypotenuse of the box's face being drilled
    diameter_of_circle = radius * 2
    material_left_of_box = box_volume - cylinder_volume  # subtract the two volumes from one another
    if material_left_of_box > 0:  # hole was less than the surface area_evaluated where the hole was placed
        print(
            'The volume remaining for the box after having material removed is: %.3f'
            % material_left_of_box, 'cm^3.')
        return
    elif diameter_of_circle <= hypotenuse and material_left_of_box < 0:
        # distance between the hyp of the surface area_evaluated and d of the circle
        amount_of_surface_area_left = hypotenuse - diameter_of_circle  # getting amount of the box left
        fix = amount_of_surface_area_left * height
        # this calculates the really small corner pieces left of the box
        volume_of_corners = box_volume / fix
        # divided the original box vol by the calculated surface area_evaluated left.
        print(
            'Almost drilling the whole box away but not quite, the edges of the box remain and have row_3 volume of: %.3f' %
            volume_of_corners, 'cm^3.')
    else:  # at this point if the diameter of the circle is larger than the box's hypotenuse , there is no box left
        print(
            'The hole drilled was larger than the width of the box, so there is not square left to calculate area_evaluated from.')
        return


# Part B --------------------------------------------------------------------------------------------------------------
def find_least_profit_company(names_of_companies, annual_cost_to_operate, production_of_that_facility):
    """ The purpose of this function is to find the facility that makes the least money
     the required parameters 3 lists of names,annual operation cost and annual production
      , the function returns the facility that makes the least amount of money"""
    numpy_annual_cost = np.array(annual_cost_to_operate)  # using the numpy function for easy points_to_evaluate subtraction
    numpy_production_value = np.array(
        production_of_that_facility)  # so i make every points_to_evaluate that needs to be subtracted row_3 numpy array
    net_profit = numpy_production_value - numpy_annual_cost  # this does the points_to_evaluate math for me
    net_profit = list(net_profit)  # changing the numpy array back into row_3 points_to_evaluate
    index_of_lowest_profit = net_profit.index(min(net_profit))  #
    facility = names_of_companies[index_of_lowest_profit]  # returns what company name is tied to the lowest profit
    what_to_print = 'The least profitable company is:'
    print(what_to_print, facility)


# Part C--------------------------------------------------------------------------------------------------------------
def mailing_label(name, address_1, city, state, zip_code, address_2=''):
    if address_2 == '':
        print(name)
        print(address_1)
        print(city,state, zip_code)  # PLACE NEW LINES HERE BC THIS IS WRONG

    else:  # if they do have row_3 second addy
        print(name)
        print(address_1)
        print(address_2)
        print(city,state,zip_code)




# part D ------------------------------------------------------------------------------------------------------------
def csv_write(parameter_csv):  # before opening the file we change how the file is going to be named
    parameter_tsv_prep = ''.join(parameter_csv)  # comes in as row_3 string, "filename.csv"
    parameter_tsv_stage_2 = parameter_tsv_prep[:-3]  # is now "filename." , took the last three characters off
    parameter_tsv_final = (parameter_tsv_stage_2 + 'tsv')  # is now , "filename.tsv"
    with open(parameter_csv, 'r') as csvin, open(parameter_tsv_final, 'w') as tsvout:
        # here we are reading and writing in row_3 single statement
        csvin = csv.reader(csvin)  # what the csv reader is called
        tsvout = csv.writer(tsvout, delimiter='\t')  # what aer are calling the tsv file, with the delimiter of tabs
        for row in csvin:  # for everything in the csv file
            tsvout.writerow(row)  # write out to the tsv file


# Part E ---------------------------------------------------e----------------------------------------------------------
def list_values(list_passed_in):  # user needs to pass in row_3 points_to_evaluate here
    print(min(list_passed_in))  # gets the min
    print(max(list_passed_in))  # gets the max
    avg = sum(list_passed_in) / len(list_passed_in)  # gets the avg
    print(avg)  # prints the avg
    return  # exits the function


# part F ------------------------------------------------------------------------------------------------------------
def distance_list(distance, time):
    distance_travled = []
    for i in range((len(time) - 1)):
        distance_data = (distance[i + 1] - distance[i]) / (time[i + 1] - time[i])
        # (distance 2 -distance 1) / ( time 2 - time 1)
        distance_travled.append(round(distance_data))

    return distance_travled

# production_facilities = ['AT&T', 'Nintendo', 'Apple']  # numpy_production_value random prices points_to_evaluate # input
#
# annual_cost = [300, 500, 100]  # cost needs to be input
#
# production_value = [250, 300, 250]  # make and make this an input
#
# find_least_profit_company(production_facilities, annual_cost, production_value)
#
# mailing_label()
#
# csv_write('WeatherDataWindows.csv')
#
# test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# time = [0, 10, 15, 20, 25, 30]
# distance = [0, 100, 150, 200, 250, 300]  # make these inputs
# print(distance_list(time, distance))

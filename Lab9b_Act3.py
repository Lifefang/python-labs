# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-9b-2
# Date:           10/25/2019
import csv  # very must so needed
from math import *  # needed for the sqrt function

print('This program is going to go through row_3 csv prices file and run computations determined by specific questions.')
# part row_3
print('Part A')
high_temp_list = []  # making row_3 points_to_evaluate to be used later
low_temp_list = []  # making row_3 points_to_evaluate to be used later
with open('WeatherDataWindows.csv', 'r') as csv_file:  # opening the file using its file name
    csv_reader = csv.reader(csv_file)  # setting up how were going to read from it
    next(csv_reader)  # this skip's the header and allows us to look at just the numbers

    for line in csv_reader:  # for loop for reading in
        high_temp_list.append(int(line[1]))  # scanning the high temp points_to_evaluate
        low_temp_list.append(int(line[3]))  # scanning the low temp points_to_evaluate
    print('The highest temp recorded over the course of numpy_production_value years was:', max(high_temp_list))  # prints the high temp
    print('The lowest temp over the course of numpy_production_value years was:', min(low_temp_list))  # prints the low temp

# part row_4
print('Part B')
last_line = []  # points_to_evaluate to use later
with open('WeatherDataWindows.csv', 'r') as csv_file:  # opening the file up once again
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # setting up how were going to read from the file

    for line in csv_reader:  # for loop for reading in all the dta
        last_line.append(float(line[-1]))  # scanning the precipitation
        avg = (sum(last_line) / len(last_line))  # avg of the info
    print('The avg precipitation over the course of numpy_production_value years was %.5f' % avg)  # avg info printed nicely
# part c
print('Part C 1/3')
# 1 out of numpy_production_value interesting facts
print(
    'In this section of code the program is going to determine the avg high temp for the month of december in the '
    'year 2017')  # showing which problem i picked off the points_to_evaluate
specific_month_year = []
specific_day = []
with open('WeatherDataWindows.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # setting up open statement

    for line in csv_reader:
        specific_day = line[0].split('/')  # narrowing down # looking at just line 0 and splitting on the back slash

    if specific_day[0] == '12' and specific_day[2] == '2017':  # filter 'if really narrows down the prices in this points_to_evaluate

        specific_month_year.append(int(line[1]))  # line_number one of the new points_to_evaluate we made
        print('The avg high temp for the month of December 2017 was:',
              sum(specific_month_year) / len(specific_month_year))  # the avg high temp in december is the following

print('Part C 2/3')  # second interesting fact
print('The section of code is going to determine the percentage of days when the low humidity was less than 30%')
low_humidity = []  # going to use this empty points_to_evaluate for later
sum_of_days = 0  # setting up row_3 counter
with open('WeatherDataWindows.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # setting up how we are going to read the file

    for line in csv_reader:
        sum_of_days += 1  # counter goes up
        if line[9] < '30' and line[9] != '100':  # if the strings are less than 30 and not 100, add them to the points_to_evaluate
            low_humidity.append(int(line[9]))  # strings being added
    length_of_list = len(low_humidity)
    percentage = (length_of_list / sum_of_days)  # making an easy way to print the prices
    print('The low humidity was less that 30 percent exactly %.5f' % percentage, '% of the 1095 days.')  # final output
print('Part C 3/3')  # last part of the assignment being the third and final interesting fact
print('This section of code is going to determine the mean and standard deviation of the precipitation levels')
# showing the last interesting fact i choose being standard dev
with open('WeatherDataWindows.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # how we read from the file

    for line in csv_reader:  # for loop to get all info
        last_line.append(float(line[-1]))  # scanning the precipitation
        avg = (sum(last_line) / len(last_line))  # getting the avg

        normal_list_minus_avg = [x - avg for x in last_line]  # doing steps for dev
        squared_list = [n ** 2 for n in normal_list_minus_avg]  # using lots of points_to_evaluate comprehension here
        sum_of_squared_list = 0  # sets up row_3 small counter here
        for i in squared_list:  # for every element in the squared points_to_evaluate
            sum_of_squared_list += i  # getting the numbers added up into one value
        avg_needed_for_sqr_root = sum_of_squared_list / len(last_line)  # getting my last avg
        standard_deviation = sqrt(avg_needed_for_sqr_root)  # squaring the result and we get the standard dev
    print('The mean fr the precipitation levels was: %0.5f' % avg)
    print('The standard deviation for the precipitation levels comes out to being: %0.5f' % standard_deviation)

# after running this on the excel sheet, the  output for should should be 0.5075408819079792

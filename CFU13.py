# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#13
# Date:           11/20/2019

# ----------------------------------------------------------------------------------------------------------------------

# first we are going to start off by defining the function leap year
# part 1 is going to define a function that does all the work for us


def leap_years(start_year, end_year):
    '''This function is going to calculate leep years based on the parameters that are passed into the function
    if the year is divisible by 4 it is a leep year, if the year is divisible by 100, it must be dividable by 400 to be a leap year
    this function will then return a list of the valid years that are leap years'''

    valid_years = []  # this is a list that will be filled with valid years if the years meet the criteria
    not_valid = []
    for year in range(start_year, end_year + 1):  # range of the year we want INCISIVE and up too!
        if year % 4 == 0:
            valid_years.append(year)  # if mod by 4 = 0 then append
        elif year % 100 == 0:  # if mod 100 == 0 and mod 400 == 0 it will append if not do nothing really
            if year % 400 == 0:  # making it specific
                valid_years.append(year)  # will append the very specif year we need
            else:
                not_valid.append(year)  # will never be used again just setting it up
    return valid_years  # returning the list of valid years


# ----------------------------------------------------------------------------------------------------------------------

# in part 2 we are going to read in from a file that will have a list of years and pass them into leap years
with open('LeapDates.txt', 'r',delimiter = '\n')as filein:  # setting up the portion of code where we are reading in
    # from a file
    # delimiter needs to be set up because the values are separated by commas
    data = filein.readlines()  # prices is not a list of ALL the years that the file contains

data = [int(i) for i in data]  # using list comprehension prices is now a list of ints so we can do math on the numbers

start_year = data[0]  # this is the start of the list , first parameter
end_year = data[-1]  # this is the very last element of the list and the last parameter we need

# ----------------------------------------------------------------------------------------------------------------------

# in part 3 we are now going to invoke the function leap_years and pass the list of valid years to a file titled
# 'LeapYearRanges.txt’
with open('LeapYearRanges.txt', 'w')as f:  # opening the file we are going to write to
    what_to_write = leap_years(start_year, end_year)  # passing in and calling the parameters , then assigning it to a
    # variable
    for i in what_to_write: # what to write us a list that equals the returned list of valid years that are leap years
        f.write(str(i)+',')  # writing the string of the valid years that were returned from the invoked function
# this is the end of the program

# ----------------------------------------------------------------------------------------------------------------------

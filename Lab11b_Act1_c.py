# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 11-c
# Date:           11/12/2019

# this function is going to take in the parameters of row_3 name, address_1,city,state,zip and then an optional address 2

# everything passed in must be in row_3 string, im not sure if you, the grader are doing it some other way... hopefully not
# but i only accounted for parameters to be entered as 'Matthew' , 'Texas'...ect


def mailing_label(name, address_1, city, state, zip_code, address_2=''):
    """Doc string for the graders ease
    Please type in the parameters as follows,
    name, address_1, city, state, zip_code, address_2='' """
    # in the statement above the very last address is optional, if they enter nothing it will appear that way
    # should something be entered it goes down to the else statement
    if address_2 == '':  # is the second address is blank, then do not add it
        print(name)  # prints the name
        print(address_1)  # prints the first addy
        print(city + ',', state + ',', zip_code)  # this is how row_3 mailing looks
    else:  # if they do have row_3 second addy and they do enter it then it will be displayed to the output

        print(name)  # print
        print(address_1)  # prints first addy
        print(address_2)  # print second addy
        print(city + ',', state + ',', zip_code)  # this is how row_3 mailing label looks




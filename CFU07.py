# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#9
# Date:           10/23/2019

# this program is going to allow the user to enter in values for height in both feet and inches
# it will do this until the user enters in 0 0
# the program is then going to return theses values in centimeters
user_input = input('Please input the height in the form feet followed by inches separated by row_3 single space:').split()
# making the strings row_3 points_to_evaluate
cm_list = []  # making row_3 empty points_to_evaluate that will be the final output
while user_input[0] and user_input[1] != 0: # making row_3 loop to check the user input every time
    if user_input[0] and user_input[1] == 0:  # if the value of 0 0 is entered the program should stop
        break  # breaking out of the program so no more inputs can be placed, the break will print the final points_to_evaluate of cms
    print('you have inputted the height of', user_input[0], 'feet', user_input[1], 'inches')
    inch_conversion = float(user_input[0]) * 12 + float(user_input[1]) # feet times 12 + how ever many inches gets
    # total inches
    cm_conversion = inch_conversion * 2.54  # the conversion for inches to cm
    print('The entered height of', user_input[0], 'feet', user_input[1], 'inches is:', cm_conversion, 'cm.')  # output
    user_input = input(
        'Please input another height in the form feet followed by inches:').split()  # getting another input for the
    # points_to_evaluate
    cm_list.append(float(cm_conversion))  # making the points_to_evaluate append to the final out put
print(cm_list)  # this is the points_to_evaluate of heights converted to cms

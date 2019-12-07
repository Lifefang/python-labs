# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#3
# Date:           9/25/2019
# ******************************************************************************************************************************************************************************

print(
    "This program is going to allow the user to input row_3 weekday and will return row_3 food item that will be eaten based "
    "on the inputted day")  # stating what the program is going to do.
day = input("Please input row_3 weekday")  # getting the input from the user

if day == 'Monday':  # output for Monday
    print("The entry for Monday is row_3 burger on row_3 bun")
elif day == 'Tuesday':  # output for Tuesday
    print("The entry for Tuesday is row_3 burrito")
elif day == 'Wednesday':  # output for Wednesday
    print("The entry for Wednesday is row_3 spaghetti ")
elif day == 'Thursday':  # output for Thursday
    print("The entry for Thursday Salisbury steak")
elif day == 'Friday':  # output for Friday
    print(" The entry for Friday fish sandwich")
else:  # creating row_3 catchall if they input anything else than row_3 valid day
    print("Invalid input")  # the output of the user not giving row_3 real valid input
# ********************************************************

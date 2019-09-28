# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     CFU-#3
# Date:           9/25/2019
#******************************************************************************************************************************************************************************

print("This program is going to allow the user to input a weekday and will return a food item that will be eaten based on the inputted day") #  stating what the program is going to do.
day = input("Please input a weekday")  #  getting the input from the user

if day == 'Monday': #  output for Monday
    print("The entry for Monday is a burger on a bun")
elif day == 'Tuesday': #  output for Tuesday
    print("The entry for Tuesday is a burrito")
elif day == 'Wednesday': #  output for Wednesday
    print("The entry for Wednesday is a spaghetti ")
elif day == 'Thursday': #  output for Thursday
    print("The entry for Thursday Salisbury steak")
elif day == 'Friday': #  output for Friday
    print(" The entry for Friday fish sandwich")
else: # creating a catchall if they input anything else than a valid day
    print("Invalid input") #  the output of the user not giving a real valid input
#********************************************************
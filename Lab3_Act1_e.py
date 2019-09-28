# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 3, Act 1
# Date:           9/10/2019

# This program converts number of Miles per Hour to Meters per Second
print("This program converts number of miles per hour to number of meters per second")
Miles_Per_Hour_Input = float(input("Please enter the number of miles per hour to be converted to meters per second:"))
Meters_Per_Second_Output = (Miles_Per_Hour_Input * 0.44704)  # 1 mile per hour is equivalent to 0.44704 meters per
# second
print(str(Miles_Per_Hour_Input)+" Milers per hour is equivalent to",str(Meters_Per_Second_Output) + "Meters per "
                                                                                                    "second.")

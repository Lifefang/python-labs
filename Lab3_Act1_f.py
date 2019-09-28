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

# This program converts number of Fahrenheit to Celsius
print("This program converts the temperature from fahrenheit to celsius")
Fahrenheit_Input = float(input("Please enter the temperature in fahrenheit you wish to convert into degrees celsius:"))
Celsius_output = (Fahrenheit_Input - 32) * 5 / 9  # one degree in fahrenheit is equal to (F -32)* 5/9
print(str(Fahrenheit_Input) + " degrees Fahrenheit is equivalent to", str(Celsius_output) + " degrees celsius.")

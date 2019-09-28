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

# This program converts number of Pascals to Millimeters of Mercury
print("This program converts number of pascals to number of millimeters of mercury")
Pascals_input = float(input("Please enter the number of pascals to be converted to millimeters of mercury:"))
Millimeters_of_Mercury_output = (Pascals_input * 0.00750062)  # 1 pascale is equal mmhg
print(str(Pascals_input) + " pascals is equivalent to", str(Millimeters_of_Mercury_output) + " millimeters of mercury.")

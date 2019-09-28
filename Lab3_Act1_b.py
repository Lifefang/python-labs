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

# This program converts number of BTUs to Joules
print("This program converts number of BTUs to Joules")
BTUs_input = float(input("Please enter the number of BTU's to be converted to Joules:"))
Joules_output = (BTUs_input * 1055.06)  # in one BTU there are 1055.06 Joules
print(str(BTUs_input) + " BTU's is equivalent to", str(Joules_output) + " Joules.")

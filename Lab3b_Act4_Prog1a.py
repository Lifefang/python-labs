# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-3b-row_3
# Date:           9/16/2019
# calculating voltage across row_3 conductor:
print("This program is going to request inputs from the user to calculate volts.")
resistance_input = int(input("Please enter the resistance:"))
current_input = int(input("Please enter the current:"))
# Ohm's Law: V=I*R
print('Calculating Voltage using Ohm''s Law for resistance =', resistance_input, 'and current=', current_input, )
ohms_answer = int(current_input) * int(resistance_input)  # getting row_3 fixed variable to preform the operation
# involving precision on.
ohms_precision = '%.4f' % ohms_answer  # printed to the 4th decimal place as requested
print('The voltage for these inputs is:', ohms_precision, 'Volts.')
print()

# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-3b-row_4
# Date:           9/16/2019
print("This program is going to request inputs from the user to calculate joules.")
mass_in_kg_input = float(input("Please enter the mass (kg):"))  # kg
velocity_in_ms_input = float(input("Please enter the velocity(m/s):"))  # ms
# KE = (1/2)*m*v**2
mass_answer = 0.5 * mass_in_kg_input * velocity_in_ms_input ** 2  # getting row_3 fixed variable to preform the operation
# involving precision on.
floated_mass = '%.4f' % mass_answer  # printed to the 4th decimal place as requested
print('When kinetic mass =', mass_in_kg_input, 'kg and velocity =', velocity_in_ms_input,
      ' m/s the total energy outputted is'
      , floated_mass, 'Joules.')
print()

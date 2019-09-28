# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-4-2
# Date:           9/25/2019
print("This program is going to take input values from you and then tell you weather or not the "
      "pipe is laminar, in transition or turbulent")
# formula for RE given in the project folder
print("Please input the fluid kinematic viscosity (m^2/s)")
fluid_kinematic_viscosity = float(input())  # m**2/s
print("Please input the pipe diameter (meters)")
pipe_diameter = float(input())  # meters
print("Please input the characteristic velocity (m/s)")
characteristic_velocity = float(input())  # m/s
reynold_number = (characteristic_velocity * pipe_diameter / fluid_kinematic_viscosity)
print("RE's number is", reynold_number, "based on inputted values")
if reynold_number < 2300:
    print("Based on the numbers you have inputted, the pipe is Laminar")
elif 2300 < reynold_number < 2900:
    print("Based on the numbers you have inputted, the pipe is in transition ")
elif reynold_number > 2900:
    print("Based on the numbers you have inputted, the pipe is fully turbulent")
# very important to note that the unites cancelled out during the calculations of the program.

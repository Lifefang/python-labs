# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-2B
# Date:           9/10/2019
from math import *

print()
# part A
# Including UIN
print("Part A")
print("Matthew Rodriguez\n729007312\n537")
print()

# Part B
# Interesting fact
print("Part B")
print('Interesting fact: I cant wait to be in college station .')
print()

# Part C
# calculating voltage across row_3 conductor:
resistance = 20
current = 5
# Ohm's Law: V=I*R
print('Part C)')
print('Calculating Voltage using Ohm''s Law for resistance = 20 and current = 5')
print('The voltage for this is ;', current * resistance, 'Volts.')
print()

# Part D
# Calculating Kinetic Energy:
mass_in_kg = 100  # kg
velocity_in_ms = 21  # ms
# KE = (1/2)*m*v**2
print('Part D)')
print('The KE for mass = 100 and velocity = 21 is;', 0.5 * mass_in_kg * velocity_in_ms ** 2, 'N.')
print()

# Part E
# Calculating Reynolds Number
fluid_velocity_in_ms = 100  # ms
length_in_meters = 2.5  # in meters
Kinematic_viscosity = 1.2  # [m^s/s]
# RE= Velocity*Length/Kinematic
print('part E)')
print('Reynolds number is:', fluid_velocity_in_ms * length_in_meters / Kinematic_viscosity, '.')
print()

# Part F
# Calculating Arps list_of_evaluated_areas
initial_oil_production_bpd = 100  # bpd
arps_b_coefficient = 0.8
initial_decline_rate_bpd = 2  # bpd
time_in_days = 20  # days
# Arps list_of_evaluated_areas = initial_oil_production_bpd
# /(1+arps_b_coefficient*initial_decline_rate_bpd*time_in_days)**(1/arps_b_coefficient)
print('Part F)')
print('The Arps list_of_evaluated_areas foresees the production rate being:',
      initial_oil_production_bpd /
      (1 + arps_b_coefficient * initial_decline_rate_bpd * time_in_days) ** (1 / arps_b_coefficient),
      'barrels per day.')
# reformatted the line_number for readability
print()

# Part G
# Calculating Mohr-Coulomb Failure Criterion
normal_stress = 20  # [Lbf/in^2]
angle_in_deg = 35  # must be converted to radians
cohesion = 2  # [Lbf/in^2]
# Mohr-Coulomb Failure Criterion list_of_evaluated_areas is: T = (normal_stress * tan(radians(angle_in_deg)) + cohesion)
print('Part G)')
print('The calculated sheer stress is:', (normal_stress * tan(radians(angle_in_deg)) + cohesion), '.')

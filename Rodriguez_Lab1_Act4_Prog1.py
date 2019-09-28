# By submitting this assignment, I agree to the following:

#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-1B
# Date:           8/28/2019
from math import *

print('Interesting fact: I went to state playing the bari Sax.')
print()

# Part C
# calculating voltage across a conductor:
r = 20
i = 5
# Ohm's Law: V=I*R
print('Part C)')
print('Calculating Voltage using Ohm''s Law for resistance = 20 and current = 5')
print('The voltage for this is ;', i * r, 'Volts.')
print()

# Part D
# Calculating Kinetic Energy:
m = 100  # [Kg}
v1 = 21  # [m/s]
# KE = (1/2)*m*v**2
print('Part D)')
print('The KE for mass = 100 and velocity = 21 is;', 0.5 * m * v1 ** 2, 'N.')
print()

# Part E
# Calculating Reynolds Number
V2 = 100  # [m/s]
L = 2.5  # [m]
K = 1.2  # [m^s/s]
# RE= V2*L/K
print('part E)')
print('Reynolds number is:', V2 * L / K, '.')
print()

# Part F
# Calculating Arps equation
qi = 100  # [Bpd]
b = 0.8
Di = 2  # [Bpd]
t = 20  # [Days]
# Arps equation = qi/(1+b*Di*t)**(1/b)
print('Part F)')
print('The Arps equation foresees the production rate being is:', qi / (1 + b * Di * t) ** (1 / b), 'barrels a day.')
print()

# Part G
# Calculating Mohr-Coulomb Failure Criterion
o = 20  # [Lbf/in^2]
oi = 0.6108652382  # [Radians] converted the degree of 35 to radians
c = 2  # [Lbf/in^2]
# Mohr-Coulomb Failure Criterion equation is: T = o tan (oi)+c
print('Part G)')
print('The calculated sheer stress is:', (o * tan(oi) + c), '.')

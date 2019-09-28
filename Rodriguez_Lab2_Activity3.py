# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 2, Act 3
# Date:           9/10/2019

print('Part 1')
# The formula using linear interpolation to find how many meters past the starting line the car has traveled between
#  30 - 45 seconds is (113/3)*( 'seconds_past_arrival' - 30)+50
seconds_past_arrival = 37  # seconds
meters_past_starting_line = ((113/3)*(seconds_past_arrival - 30)+50)  # meters
print('The distance the car will be past the starting line' , seconds_past_arrival , 'seconds after your arrival will be', meters_past_starting_line, 'meters.')
# Question: If you input 0 as a time you will get -1080 meters and this is not right. With the formula used you
# can only input values between 30 and 45 seconds to get reliable answers. If you plot a graph using the given
# information you can easily make predictions because it is a line, but to use linear interpolation correctly you
# cant assume the line is straight outside your given values. Also, time at 0 seconds is not when the race began, it is
# the time you arrived at the race.
print()

print('Part 2')
# For this part you can use the same equation as before but divide by mod(%) 3141.59265359
seconds_past_arrival = 1200  # seconds
circumference_of_track = 3141.59265359  # meters
meters_past_starting_line = ((113/3)*(seconds_past_arrival - 30)+50) % circumference_of_track
print('The distance the car will be past the starting line' , seconds_past_arrival , 'seconds after your arrival will be', meters_past_starting_line, 'meters.')
# Questions:
#   1. This is linear extrapolation because we are using time values not between 30 to 45 seconds. We can use it
# in this scenario because we know the speed of the car is constant and that allows us to use time values that are
# beyond 45 seconds.
#   2. The code for part 2 will be to equal part 1 if we enter 37 seconds. The only difference in the two codes is one
# is on a circular track and can only reach a certain distance from the starting line before it is reset,
# while the other could be driving away from the starting line forever.

# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-2B Prog-c
# Date:           9/10/2019

# position of t1 = (range_1,y1,z1) in meters.
# position of t2 = (range_2,y2,z2) in meters.
# t0 can be found by t1<t0<t2 but must be done numpy_production_value times to obtain (x0,y0,z0) in meters.
print("----------------------------------")
time_of_interest = 20  # seconds
first_time_observed = 13  # seconds
second_time_observed = 84  # seconds
# Linear interpolation for x0 lies in the middle of points (t1,range_1),(t2,range_2)
x0 = (22 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 1
# Linear interpolation for y0 lies in the middle of points (t1,y1),(t2,y2)
y0 = (-8 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 3
# Linear interpolation for z0 lies in the middle of points (t1,z1),(t2,z2)
z0 = (3 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 7
print('time of interest at', time_of_interest, 'seconds')
print('line_number(0) =', x0, 'm')
print('y(0) =', y0, 'm')
print('z(0) =', z0, 'm')
print("----------------------------------")
time_of_interest = 27.5  # seconds
first_time_observed = 13  # seconds
second_time_observed = 84  # seconds
# Linear interpolation for x0 lies in the middle of points (t1,range_1),(t2,range_2)
x0 = (22 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 1
# Linear interpolation for y0 lies in the middle of points (t1,y1),(t2,y2)
y0 = (-8 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 3
# Linear interpolation for z0 lies in the middle of points (t1,z1),(t2,z2)
z0 = (3 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 7
print('time of interest at', time_of_interest, 'seconds')
print('line_number(0) =', x0, 'm')
print('y(0) =', y0, 'm')
print('z(0) =', z0, 'm')
print("----------------------------------")
time_of_interest = 35  # seconds
first_time_observed = 13  # seconds
second_time_observed = 84  # seconds
# Linear interpolation for x0 lies in the middle of points (t1,range_1),(t2,range_2)
x0 = (22 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 1
# Linear interpolation for y0 lies in the middle of points (t1,y1),(t2,y2)
y0 = (-8 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 3
# Linear interpolation for z0 lies in the middle of points (t1,z1),(t2,z2)
z0 = (3 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 7
print('time of interest at', time_of_interest, 'seconds')
print('line_number(0) =', x0, 'm')
print('y(0) =', y0, 'm')
print('z(0) =', z0, 'm')
print("----------------------------------")
time_of_interest = 42.5  # seconds
first_time_observed = 13  # seconds
second_time_observed = 84  # seconds
# Linear interpolation for x0 lies in the middle of points (t1,range_1),(t2,range_2)
x0 = (22 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 1
# Linear interpolation for y0 lies in the middle of points (t1,y1),(t2,y2)
y0 = (-8 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 3
# Linear interpolation for z0 lies in the middle of points (t1,z1),(t2,z2)
z0 = (3 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 7
print('time of interest at', time_of_interest, 'seconds')
print('line_number(0) =', x0, 'm')
print('y(0) =', y0, 'm')
print('z(0) =', z0, 'm')
print("----------------------------------")
time_of_interest = 50  # seconds
first_time_observed = 13  # seconds
second_time_observed = 84  # seconds
# Linear interpolation for x0 lies in the middle of points (t1,range_1),(t2,range_2)
x0 = (22 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 1
# Linear interpolation for y0 lies in the middle of points (t1,y1),(t2,y2)
y0 = (-8 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 3
# Linear interpolation for z0 lies in the middle of points (t1,z1),(t2,z2)
z0 = (3 / (second_time_observed - first_time_observed)) * (time_of_interest - first_time_observed) + 7
print('time of interest at', time_of_interest, 'seconds')
print('line_number(0) =', x0, 'm')
print('y(0) =', y0, 'm')
print('z(0) =', z0, 'm')
print("----------------------------------")

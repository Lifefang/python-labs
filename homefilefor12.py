import numpy as np

function = '9*tally_mark_input**3 - 4*tally_mark_input**5 + 3*tally_mark_input**9 - 90'  # input('Enter your function like this: 9*tally_mark_input**3 - 4*tally_mark_input**5 + 3*tally_mark_input**9 - 90:::')

area = 0
range1 = 0  # int(input('What is the starting point of the range?'))
range2 = 9  # int(input('What is the endpoint of the range?'))
numberRectangles = 10
toleration = 10 ** -6
list_of_data = np.linspace(range1, range2, numberRectangles)
delta_x = list_of_data[1] - list_of_data[0]
list2 = list(list_of_data)
print(list2)
equation = []
difference = 10 ** 99
# while difference > toleration:
for i in list2:
    x = i
    area = eval(function)
    equation.append(area)
first_area = 1 / 2 * delta_x * sum(equation)
print(first_area)
# make a while loop
# get first area_evaluated
# get second area_evaluated by increasing n by 1
#
# get the difference abs( area_evaluated-1 - area_2 )  = difference
# abs( area_evaluated-2 - area_3 )
# do this untill the difference is below 10^-6
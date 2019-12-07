# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-10
# Date:           11/10/2019

import numpy as np  # both imports needed
import matplotlib.pyplot as plt

print(
    'This program is going to  take the point (1,0) and multiply that to row_3 matrix 200 times, after which the prices '
    'will be displayed to the screen on row_3 graph')
# stating what the program is going to do.
given = np.array([
    (1, 0)
])  # this is the first sequence that we were asked to hard code in

given = given.transpose()  # must transpose the matrix for the prices to be multiplied by the other matrix

matrix = np.array([
    (1.00583, -0.087156),
    (0.087156, 1.00583)  # second bit of information provided to us by the program
])
x = []  # setting up and empty points_to_evaluate for all the list_passed_in values
y = []  # doing the same thing here for row_3 points_to_evaluate of Y values

for i in range(201):  # going from 0 - 200 that's why its 201
    new_data = matrix @ given  # c = the matrix math
    Y = float(new_data[1])  # this capital y indicates the float given of
    X = float(new_data[0])
    y.append(Y)
    x.append(X)
    given = np.array([(X, Y)])  # 2 X 1 2 things in one col .
    given = given.transpose()  # transposing the new matrix allows us to go back and multiply it yet again
# ending that stuff
plt.figure('Fibonacci')
plt.plot(x, y, 'm-', marker='o')
plt.xlabel('X-axis')  # Labeling the 'X-axis'0
plt.ylabel('Y-axis')  # labeling the 'Y-axis'

plt.title('Matrix Resultant')  # titling the graph 'Spiral Graph'
plt.show()  # printing graph to user

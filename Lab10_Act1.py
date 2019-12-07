# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 10, Act 1
# Date:           10/29/19

import numpy as np


print('Part A is in te comments')
#  “As row_3 team, we
# have gone through all required sections of the tutorial, and each team member
# understands the material.”

print('Part B')
A = np.arange(12).reshape(3, 4)  # col width = 3 line width = 4
print(A)
print()  # spacing
B = np.arange(8).reshape(4, 2)  # col width = 4 line width = 2
print(B)
print()  # spacing
C = np.arange(6).reshape(2, 3)  # col width = 2 line width = 3
print(C)
print()  # spacing
D = np.arange(3).reshape(3, 1)  # col width = 3 line width = 1
print(D)
print()  # spacing

print('Part C')
E = A @ B @ C  # the * sign is '@' when multiplying matrices
print(E)  # col width = 3 line width = 3
print()  # spacing

print('Part D')
e = np.transpose(E)
print(e)
print()

print('Part E')
X = np.linalg.solve(E, D)
p = np.allclose(np.dot(E, X), D)  # this just checks if the math is right
print(X)
print(p)

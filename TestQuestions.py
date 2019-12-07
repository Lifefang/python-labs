# user_input_1 = input('Please input row_3 number here')
# user_input_2 = input('Please input row_3 number here')
# user_input_3 = input('Please input row_3 number here')
# user_input_4 = input('Please input row_3 number here')
# user_input_5 = input('Please input row_3 number here')
# number_of_inputs = 5
# my_set = set()
# my_set.update(user_input_1,user_input_2,user_input_3,user_input_4,user_input_5)
# if len(my_set)!= number_of_inputs:
#     print('dups found')
# else:
#     print('all unique')
#     #
# list_ages = []
# list_names = []
# age = int(input('please put an age here:'))
# while age > 0:
#     list_ages.append(age)
#     name= input('please input row_3 name for that age')
#     list_names.append(name)
#     age = int(input('please put another age here:'))
# avg_age = sum(list_ages)/len(list_ages)
# print(avg_age)
# old = list_ages.index(max(list_ages))
# oldest_person=list_names[old]
# young = list_ages.index(min(list_ages))
# youngest_person=list_names[young]
# #3

import matplotlib.pyplot as plt
import numpy as np
from math import *

x = float(input('Please input a value for x:'))
s = float(input('Please input a value for s:'))
u = float(input('Please input a value for u:'))
value = 0


def computation(x, u, s):
    p_of_x = 1 / sqrt(2 * pi * s ** 2) * np.exp(-(x - u) ** 2 / 2 * s ** 2)
    value = p_of_x
    return value


print('The value for the function when x=', x, 's=', s, 'and when u =', u, 'is', computation(x, u, s))

new_x = np.linspace(-3, 3, 100)
y = []
for i in new_x:
    Y = computation(i, 0, 1)
    y.append(Y)
plt.plot(new_x, y, label='The function')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()


from math import *

# n = 7  # num -1
# for i in range(2, num):
#     if num % i == 0:
#         print(num, 'is not prime')
#         break
# else:
#     print(num, "is prime")
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     else:
#         return True
#
#
# def lpf(n):
#     x = []
#     for i in range(2, n):
#         if prime(i):
#             if n % i == 0:
#                 x.append(i)
#     return x
#
#
# print(lpf(600851475143))

# this is where i showed what it was gonna do
# troys test question
# num_list = []
#
#
# def perfect_num(x):
#     for i in range(1, x):
#         if x % i == 0:
#             num_list.append(i)
#
#     if sum(num_list) == x:
#         return True
#     else:
#         return False
#
#
# print(perfect_num(28))
# print(num_list)
# ------------------Go over this too way to long
# prices = []
# item_number = []
# with open('item_cost.dat', 'r', )as f:
#     next(f)
#     for line in f:
#         prices.append(line[6:10].strip())
#         item_number.append(line[0:5].strip())
# print(item_number)
# print(prices)
# prices = [float(i) for i in prices]
# print(prices)
# min = 100.00
# for i in prices:
#     if min > i:
#         min = i
# print(min)
# index_of_occurance = prices.index(min)
# lowest_price = item_number[index_of_occurance]
#
# print('The item with the lowest price is', lowest_price,'Which is:',min)
# ---------------------------------

# writing a program that is going to input data as entered by the user.

# getting the first input
# file_name = input('Please input a file name INCLUDING the file exstention:') # getting the files name
#
# # now getting the number of data entries we are going to take in
# data_entries = int(input('Please input the number of data entries you will input:')) # getting how many entiries there are
#
# # now getting all that data right here
# name = []
# data = [] # making two blank lists to use further on in the code
# while len(data) != data_entries: # while we dot have all the data entires
#     print('lets get all the data we need right here') # just a message to the user
#     name_to_get = input('please insert the name of the student that made the score') # getting the name
#     data_to_get = float(input('Please inster the score this student made:')) # getting their score
#     name.append(name_to_get)
#     data.append(data_to_get) # appending all this to list
# mean_of_data = sum(data)/data_entries    # gettung the avg
# data_for_file = [str(i) for i in data] # making all this data a string
#
#
# counter = 0 # counter goes up every time
# with open(file_name,'w') as file: # opening that file
#     file.write('Names \t Score \n') # printing the header
#     for i in range(data_entries): # up till the point we wanna evaluate
#         file.write(name[counter] + '\t'+ data_for_file[counter] + '\n') # this is what where writing
#         counter +=1 # going up for the list
# prnt('The avg score for this test was %.1f' % mean_of_data) # what was requested to print at the end of this assigenmenti

# for i in range(5):
#     i = 4/2 *(i+2)
#     for j in range(i):
#         print(j)
#         break
# from matplotlib import pyplot as plt
# import numpy as np
# from math import *  # importing the modules needed
#
# xsin = []
# x_cos = []
#
# domain_of_graph = np.linspace(0, 4 * pi, 100)
# for x in domain_of_graph:  # this straight up graphs cos and sin from 0 - 4 pi
#     x_1 = sin(x)
#     xsin.append(x_1)
#     x_2 = cos(x)
#     x_cos.append(x_2)
#
# x_list = [pi / 4, 5 * pi / 4, 9 * pi / 4, 13 * pi / 4]
# y_list = []
# for i in x_list:  # this gets the points of intersection
#     Y = sin(i)
#     y_list.append(Y)
# plt.plot(domain_of_graph, xsin, color='b', linestyle='--')
# plt.plot(domain_of_graph, x_cos, color='g')
#
# plt.plot(x_list, y_list, 'o')
# plt.xlabel('Y-Axis')
# plt.ylabel('X-Axis')
# plt.title('Here the graph')
# plt.show()
# -------------------------------------------------------------------------------------------------------------------
#
# store = {'apple': 2.89, 'grapes': 5.12, 'orange': 2.09}
# store['banna']= 2.89
# print(store)
my_list = [1, 2, 5, 4, 22, 6]
answer = my_list[-3:0:-2]
print(answer)
p
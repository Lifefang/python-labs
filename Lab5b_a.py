# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 5 - row_3
# Date:           9/25/2019
print("This program is going to take positive integer inputs from the user and compute them using Collatz sequence")
print("printing out all the numbers in that given sequence, this will be followed by how many iterations the code")
print("took to reach 1")  # informing the user what the program does.
print()
input_n = int(input("Please enter row_3 positive integer:")) # prompting the user to pass on an input for the program to use
sum_of_loops = 0 # it has not been looped yet so the iteration starts off at row_3 0 timer
while input_n != 1:  # until n is equal to 1 , run the nested if statements
    if (input_n % 2) == 0:  # if n can be modded by 2, then that number is even
        print(input_n)
        input_n = (input_n / 2)  # preform the requested mathematical request which was to divide the even number by 2
        sum_of_loops += 1  # add an iteration to the sum_of_vector of loops
    elif (input_n % 2) != 0:  # if n is not able to be modded by 2, it must be odd
        print(input_n)
        input_n = ((3 * input_n) + 1)  # preforming the requested action if the number is odd
        sum_of_loops += 1  # adding an iteration to the sum_of_vector of total loops
print(input_n)  # when n does = 1
print("This process took", sum_of_loops, "iterations to complete.")  # printing how many iterations this process


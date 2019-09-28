# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 5 - b
# Date:           9/25/2019
print("This program is going to ask the user to input a positive number and will then do two things.")
print("The program is going to out put the sum off all numbers from 0 to the input")
print("The program will also find the product off all numbers from 0 to the input")
print()
# showing what the program is going to do
user_number = int(input("Please enter a positive integer number:"))
i = 0
sum = 0
user_number = user_number + 1  # this number needs to be increased by one because we want are equation to take into
# account that value
# not just the value under it
for i in range(user_number):
    sum = sum + i  # this allows the sum to add it self to the iterations
    i += 1
print("The sum of all integers from 0 to", user_number - 1, " in a for loop is:", sum)  # this is for the "for" loop
sum = sum
new_sum = 0
i = 0
# making it easier on the eyes to look at for grading purposes
while i != user_number:
    new_sum = new_sum + i  # new sum was added to make sure that the old sum was not simply being printed out
    i = i + 1  # i still need to go up an iteration, until it is equal to the users number
print("The sum of all integers from 0 to", user_number - 1, "in a while loop is:", new_sum)  # this is for a
# "while" loop
# now this section will be to get the product of all integers from 1 through the number entered
i = 1  # i is now one because 0 times the loop will out put a 0
sum = 1
for i in range(1, user_number):
    sum = sum * i  # this time the sum is being multiplied
    i = i + 1
print("The product of all integers from 1 to", user_number - 1, "in a for loop is:", sum)
# doing the same thing but for a while loop
sum = sum  # need to carry over this vale to make calculations
new_sum = 1  # new sum was added to make sure that the old sum was not simply being printed out
i = 1  # must be set to 0 as anything times 0 is 0
while i != user_number:
    new_sum = new_sum * i  # this time the sum is being multiplied
    i = i + 1  # i still need to go up an iteration, until it is equal to the users number
print("The product of all integers from 1 to", user_number - 1, "in a while loop is:", new_sum)
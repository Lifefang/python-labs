# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 3, Act 2
# Date:           9/18/2019

print("User one please enter your first and last name:")
user_one_name = str(input())  # getting user one name
print("Now please enter your birthday in the format of 00/00/0000:")
user_one_birthday = str(input())  # getting user one birthday
print("User two please enter your first and last name:")
user_two_name = str(input())  # getting user two name
print("Now please enter your birthday in the format of 00/00/0000:")
user_two_birthday = str(input())  # getting user two birthday
print("User three please enter your first and last name:")
user_three_name = str(input())  # getting user three name
print("Now please enter your birthday in the format of 00/00/0000:")
user_three_birthday = str(input())  # getting user three birthday
print("User four please enter your first and last name:")
user_four_name = str(input())  # getting user four name
print("Now please enter your birthday in the format of 00/00/0000:")
user_four_birthday = str(input())  # getting user four birthday
print()  # printed for space
print()  # printed for space
print(str(user_one_name).ljust(20), user_one_birthday)  # .ljust for left line up
print(str(user_two_name).ljust(20), user_two_birthday)  # printing the column
print(str(user_three_name).ljust(20), user_three_birthday)
print(str(user_four_name).ljust(20), user_four_birthday)

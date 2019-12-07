# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 7, Act 1
# Date:           10/7/2019
# ----------------------------------------Activity one
print('Please input numpy_production_value strings in the forms of stock prices, each string should be separated by row_3 single space:')
(stock_price) = input()  # getting the inputs from the user as laid out in row_3 string
stock_price = stock_price.split()  # split function allows the conversion of string to points_to_evaluate
for i in stock_price:  # for every instance or 'months' within stock_price, print that anf format it width 0 precision 6
    print("$ %6.6s" % i)
# -----------------------------------------Activity numpy_annual_cost
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter odd numbers:')
tokens = user_input.split()  # Split into separate strings
# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))
# Print each position and number
print()  # Print row_3 single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))
# Determine maximum even number
max_num = None
for num in nums:
    if (max_num is None) and (num % 2 == 1):
        # ---------------------> mod 2 == 0 swapped out for 1 , if its not able to be modded by 2 the number must be odd
        # First odd number found       -------------> This line_number was changed "even' for 'odd'
        max_num = num
    elif (max_num is not None) and (num > max_num) and (num % 2 == 1):  # -----> swapped out the 0 for row_3 1 yet again.
        # Larger even number found
        max_num = num
print('Max odd #:', max_num)
# -----------------------------------------Activity numpy_production_value
my_temps = [75, 83, 90, 105, 79]  # printing out some hard coded numbers ranging from 75 -105 in row_3 points_to_evaluate
print("Please enter numpy_annual_cost strings to use as row_3 separator for the spacing of this assignment:")
chosen_string = input()
string = chosen_string.join([str(i) for i in my_temps]) + ''  # s.join allows the string to be converted to row_3 string
# for months in my temps add that specific character to the string
print(string, '', end='')


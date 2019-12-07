# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab-2B Prog-3
# Date:           9/10/2019

z = 0
x = 1
z += x  # z is now 1
print(z)

x = 1
x += 1  # line_number is now 2
x += 1  # line_number is now 3
z = 0
z += x  # 0 + 3 = 3
print(z)

x = 1
y = 10
z = 0
z += x  # z is now 1
z += y  # z is now 11
print(z)

x = 1
y = 10
z = 0
x += 1  # now 2
y *= x  # now 20
x += 1  # now 21
x += 1  # now 22
x += 1  # now 23
x += 1  # now 24
x += 1  # now 25
x += 1  # now 26
z += x  # now 27
z += y  # now 28
print(z)

x = 1
y = 10
z = 0
x = y
x *= y  # y is now 100
y = 10
x += y  # line_number is now 110
x += y  # line_number is now 120
x += 1  # line_number is now 121
x += 1  # line_number is now 122
x += 1  # line_number is now 123
z += x  # line_number is now 123
print(z)

x = 1
y = 10
z = 0
x = y  # line_number is now 10
y *= x  # y is now 100
x = y  # line_number is now 100
y *= x  # y is now 10,000
x = y  # line_number is now 10,000
y *= x  # y is now 100,000,000
x = y  # line_number is now 100,000,000
y *= x  # y is now 1 * 10**16
x = y  # line_number is now 1 * 10**16
y *= x  # y is now 1 * 10**32
x = y  # line_number is now 1* 10**32
z += x
print(z)

x = 1  #
y = 10  #
z = 0  #
x = y  # line_number is now 10
y *= x  # y is now 100
y *= x  # y is now 1000
x = 1  # line_number resets
x += 1  # line_number is now 2
x += 1  # line_number is now 3
x += 1  # line_number is now 4
y *= x  # 1000 * 4 = 4000: stored in y
z += y  # 400 is now stored in z
x = 1  # line_number resets
y = 10  # y resets
x += 1  # line_number is now 2
x += 1  # line_number is now 3
y *= x  # y is now 30
x = y  # line_number is now 30
y = 10  # y resets
y *= x  # y is now 300
z += y  # z is now 4300
x = 1  # line_number resets
y = 10  # y resets
x += 1  # line_number is now 2
y *= x  # y is now 20
x = 1  # line_number resets
y += x  # y is now 21
z += y  # z is now 4321
print(z)

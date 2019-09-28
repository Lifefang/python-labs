# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 4 Act3
# Date:           9/27/19
# part a
print('Part a')
print("This program is going to take True and False inputs from the user and output what the inputted")
# what the program does
decision = input("Please input T,t or True for true or F,f or False for false:")
if decision == 'True' or decision == 'T' or decision == 't':  # Converting a from the string "True" to True
    print('Your input is true')
elif decision == 'False' or decision == 'F' or decision == 'f':  # Converting a from the string "False" to False
    print('Your input is false')
else:
    print('Invalid input')
print()

# part b
print('Part b')
print("This program is going to ask the user to input True or False values in the same manner as part A")
print("The program will then run these valuses through expressions and out put weather or not they are true/false")
print('Input True or False for a:')  # Getting the input from keyboard
aBool = input()
print('Input True or False for b:')
bBool = input()
print('Input True or False for c:')
cBool = input()  # With the input being in a string it needs to be converted to a boolean
if aBool == 'True' or aBool == 'T' or aBool == 't':  # Converting a from the string "True" to True
    a = True
elif aBool == 'False' or aBool == 'F' or aBool == 'f':  # Converting a from the string "False" to False
    a = False
else:
    a = False
if bBool == 'True' or bBool == 'T' or bBool == 't':  # Converting a from the string "True" to True
    b = True
elif bBool == 'False' or bBool == 'F' or bBool == 'f':  # Converting a from the string "False" to False
    b = False
else:
    b = False
if cBool == 'True' or cBool == 'T' or cBool == 't':  # Converting a from the string "True" to True
    c = True
elif cBool == 'False' or cBool == 'F' or cBool == 'f':  # Converting a from the string "False" to False
    c = False
else:
    c = False

print('1.', a and b and c)
print('2.', a or b or c)
print()
print('Part c')# making a true or false table for all of the out comes
print("This section is making a true or false table for the XOR statement")
# part c 1
aBool = 'F'
bBool = 'F'
if aBool == 'F' and bBool == 'F':
    print('XOR of a=F, b=F', False) # this would result in false
aBool = 'F'
bBool = 'T'
if aBool == 'F' and bBool == 'T':
    print('XOR of a=F, b=T', True) # this would result in true
aBool = 'T'
bBool = 'F'
if aBool == 'T' and bBool == 'F':
    print('XOR of a=T, b=F', True) # this would result in true
aBool = 'T'
bBool = 'T'
if aBool == 'T' and bBool == 'T':
    print('XOR of a=T, b=T', False) # this would result in false
print()
#part c 2
print("This program is running hardcoded values of true and false statements through a not,and or statement")
print("If there are an odd number of true values the statement should return true, false otherwise ")
print("Part c-2")
print(" a = true ")
print(" b = false ")
print(" c = true ")
a = bool(1)
b = bool(0)
c = bool(1)
print(((((a and b and c) or (a and (not(b or c)))) or (b and (not(a or c)))) or (c and (not(a or b)))))





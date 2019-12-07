# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Matthew Rodriguez
# Section:        537
# Assignment:     Lab 12-B
# Date:           11/16/2019

# imports

import turtle  # needed for the whole program to function
from math import *  # used for a sqrt operation in line 32 , makes the turtle go diagonal for the tally marks


# ----------------------------------------------------------------------------------------------------------------------

# Functions
def valid_user_input(x):
    """The purpose of this function is to check if the users input is valid
    The program does this by making an infinite loop until the criteria is meet, being a users int input from 0 - 100
    This function returns the requested marks that the user passed into the program, so long as they are valid """
    global requested_marks
    if 0 <= x <= 100:  # if less than 0 and greater than 100
        requested_marks = x  # pass statement
    elif x < 0 or x > 100:  # this is the false check
        requested_marks = 'Try Again'
    return requested_marks


# this function checks to see if the user input is valid

def diagonal_marks(i):
    """This function of code creates the diagonal marks for the turtle to follow.
    The function does this by directing the turtle to go right 135 degrees,
    forward 30 * sqrt 2 and finally right 225 degrees.
    This function returns commands to the turtle back in the main program. """
    alex.right(135)  # go right 135 so that we are crossing over all previous lines to the left
    alex.forward(30 * sqrt(2))  # this operation actually make the diagonal mark, travel over the previous lines
    alex.right(225)  # right 225, this corrects the position back to south, so we can make more tally marks


# this function does the diagonal marks


def row_one(i):
    """This purpose of this function is to loop over and over until the turtle has drawn 5 sets of tally marks The
    function does this by making the turtle go to a start point for row one (-10,0,) and directs the turtle using turtle
    commands.
    This function returns commands for the turtle to follow back in the main program. """
    global row_1 # must be made into a global so that the function works
    if row_1 == -1:  # we start one the first row, the row_1 value is only set to -1 so that the turtles position
        # is determined before it continues the makes marks
        alex.penup()  # don't want silly little alex drawing random things now, so we take his pen away
        alex.goto(-10, 0)  # this is the starting position for the bottom level of the tally marks
        alex.pendown()  # pen down
        alex.forward(30)  # draw one line
        row_1 += 1  # counter up so this if statement is not repeated
    else:  # this is where the bulk of the marks are really made steps will be listed for how the loop plays out
        alex.penup()  # 1) pick up the pen
        alex.goto(row_1 * 10, 0)  # 2) go to row_1 * 10,0 ( this acts as the tally_mark_input and y)
        alex.pendown()  # 3) pen down to draw
        alex.forward(30)  # 4) pen forward to draw
        row_1 += 1  # computation counter +=1


# this function is a loop that makes 5 sets of tally marks on row one


def row_two(i):
    """This purpose of this function is to loop over and over until the turtle has drawn 5 sets of tally marks on the
    second row.
    The function does this by making the turtle go to a new starting point, same x axis as row one but the
    y axis is simply higher (-10,50).
    This function returns commands for the turtle to follow back in the main program. """
    global row_2 # must be made into a global so that the function works
    if row_2 == -1:  # we have now changed to the second row. This entire block is a set up for positioning
        alex.penup()  # don't draw
        alex.goto(-10, 50)  # sets alex up parallel to the first tally mark drawn
        alex.pendown()  # draw
        alex.forward(30)  # move forward 30
        row_2 += 1  # computation += 1  so we don't repeat this code anymore
    else:
        alex.penup()  # no drawing
        alex.goto(row_2 * 10, 50)  # positioning for the next mark
        alex.pendown()  # get ready to draw
        alex.forward(30)  # go up 30 and make a vertical tally line
        row_2 += 1  # computation += 1


# this function is a loop that makes 5 sets of tally marks on row two


def row_three(i):
    """This purpose of this function is to loop over and over until the turtle has drawn 5 sets of tally marks on the
    third row.
    The function does this by making the turtle go to a new starting point, same x axis as row two but the
    y axis is simply higher than row 2's y axis (-10,100).
    This function returns commands for the turtle to follow back in the main program. """
    global row_3 # must be made into a global so that the function works
    if row_3 == -1:  # just making the tally's unified once again
        alex.penup()  # don't draw
        alex.goto(-10, 100)  # This entire block is a set up for positioning
        alex.pendown()  # getting ready to draw
        alex.forward(30)  # go up 30 and make a vertical tally line
        row_3 += 1
    else:
        alex.penup()  # don't draw
        alex.goto(row_3 * 10, 100)  # positioning for the next mark
        alex.pendown()  # getting ready to draw
        alex.forward(30)  # go up 30 and make a vertical tally line
        row_3 += 1


# this function is a loop that makes 5 sets of tally marks on row three


def row_four(i):
    """This purpose of this function is to loop over and over until the turtle has drawn 5 sets of tally marks on the
    fourth row.
    The function does this by making the turtle go to a new starting point, same x axis as row three but the
    y axis is simply higher than row three's y axis (-10,150).
    This function returns commands for the turtle to follow back in the main program. """
    global row_4 # must be made into a global so that the function works
    if row_4 == -1:  # just making the tally's unified once again
        alex.penup()  # don't draw
        alex.goto(-10, 150)  # This entire block is a set up for positioning
        alex.pendown()  # getting ready to draw
        alex.forward(30)  # go up 30 and make a vertical tally line
        row_4 += 1
    else:
        alex.penup()  # don't draw
        alex.goto(row_4 * 10, 150)  # positioning for the next mark
        alex.pendown()  # getting ready to draw
        alex.forward(30)  # go up 30 and make a vertical tally line
        row_4 += 1  # at this point the program is done and will only work cohesively to display 100 marks


# this function is a loop that makes 5 sets of tally marks on row four

# ---------------------------------------------------------------------------------------------------------------------

# brief description of the program

print()

print('This program is going to utilize turtle graphics to draw anywhere from 1 - 100 tally marks, based on the users '
      'input')

print()

# getting the users input
tally_mark_input = int(input('Please enter a number between 1-100 indicating how many tally marks a turtle named '
                             'alex can draw:'))
# making sure the input is valid
while valid_user_input(tally_mark_input) == 'Try Again':
    tally_mark_input = int(input('Invalid input, please input a value between 0 - 100:'))
print(valid_user_input(tally_mark_input))
print()  # in case they keep entering it wrong this makes it easy to read
# ----------------------------------------------------------------------------------------------------------------------

# setting up the turtle

wn = turtle.Screen()  # window for the program
TurtleSize = 20  # just making the turtle visible
alex = turtle.Turtle(shape='turtle')  # going to display a turtle to the screen
alex.right(90)  # sets up the turtle going down, this is pretty important for drawing tally marks

row_1 = -1  # all rows are very similar here
row_2 = -1  # they act as a counter and a position tracker
row_3 = -1  # rows interchange after every 25 tally marks
row_4 = -1  # they start at -1 to get the turtle align, and begin true computation at 0

for i in range(1, tally_mark_input + 1):  # 1 - how every many +1, inclusive for all the way up to, including
    if i % 5 == 0:  # if we have a 5th tally mark, make it a diagonal line.
        diagonal_marks(i)
    elif i < 25:
        row_one(i)
    elif 25 < i < 50:
        row_two(i)
    elif 50 < i < 75:
        row_three(i)
    elif 75 < i < 100:
        row_four(i)
turtle.done()

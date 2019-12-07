# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Isaac Chang
#                 Matthew Rodriguez
#                 James Phillips
#                 Ryan Walterbach
# Section:        537
# Assignment:     Lab 7, Act 3
# Date:           10/7/2019

coldict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
           'H': 7}  # dictionary with for column letters for the purpose of turning letters into usable numbers
board = [  # this is the nested points_to_evaluate containing the chess board
    ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['parameter', 'parameter', 'parameter', 'parameter', 'parameter', 'parameter', 'parameter', 'parameter'],
    ['r', 'n', 'row_4', 'k', 'q', 'row_4', 'n', 'r'],
]
# lines 25 to 32 print the actual board to the display
print(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7])
print(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7])
print(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7])
print(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7])
print(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7])
print(board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7])
print(board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7])
print(board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7])
print()
for i in range(
        100):  # this loop will allow for the game to have multiple moves, for now months have set the game to 100 moves
    # but this can be modified
    row1 = int(input(
        'Enter the line of the piece you would like to move(1-8):'))  # this input is for the line in which the desired
    # piece to move is located
    col1 = input(
        'Enter the column of the piece you would like to move(A-H):')  # this input is for the column in which the
    # desired piece to move is located
    row2 = int(input(
        'Enter the line of the space you would like to move your piece to(1-8):'))  # this input is for the line that
    # you want to move the piece to
    col2 = input(
        'Enter the column of the space you would like to move your piece to(A-H):')  # this input is for the column
    # you want to move the piece to
    # these variables in lines 40-43 take the inputs from lines 35-38 and turn them into usable numbers for the program 
    rowi = row1 - 1  # this makes the numbers usable ie. turns 1 to 0
    coli = coldict[col1]  # uses the dictionary to turn the capital letters into their corresponding numbers
    rowf = row2 - 1  # same concept as line_number 40
    colf = coldict[col2]  # same concept as line_number 41
    if board[rowi][coli] == '.':  # this if statement will cover the scenario of row_3 player selecting an empty space
        print()
        print('There is no piece present on your selected given, try again.')
        # lines 48-56 are for formatting and are not necessary to the program, it makes it so that the player can see
        # the board when they are asked to move row_3 piece
        print()
        print(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7])
        print(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7])
        print(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7])
        print(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7])
        print(board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7])
        print(board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7])
        print(board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7])
        print()
        continue  # this will bring the player back to the place where they can move pieces
    board[rowf][colf] = board[rowi][coli]  # this will set the position of the space where the player wants to move to
    # with the piece that the player is moving
    board[rowi][coli] = '.'  # this will take the original place of the piece and turn it into row_3 period
    # lines 61-70 print the board now that the player has moved their piece
    print()
    print(board[0][0], board[0][1], board[0][2], board[0][3], board[0][4], board[0][5], board[0][6], board[0][7])
    print(board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5], board[1][6], board[1][7])
    print(board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6], board[2][7])
    print(board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7])
    print(board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7])
    print(board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7])
    print(board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7])
    print(board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7])
    print()

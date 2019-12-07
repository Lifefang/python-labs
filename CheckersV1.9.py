import numpy as np


# -------------------SOME WILD FUNCTIONS THAT JUST KEEP GROWING--------------------------------------
def game_board():  # makes the game board
    print("  'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H'")
    board = [
        ['-', '-', '-', 'R', '-', '-', '-', '-'],
        ['-', '-', 'b', '-', 'B', '-', 'B', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'B', '-', 'B', '-'],
        ['-', 'B', '-', '-', '-', '-', '-', '-'],
        ['-', '-', 'R', '-', 'B', '-', 'b', '-'],
        ['-', 'B', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]
    board = np.array(board)
    return board


def update_board_with_player_move(intial_spot, final_spot):
    # this takes the initial spot and final spot the user inputs and changes the intial location back to an a dash and
    # changes the final spot into the whatever peice occupied the initial location
    row_i = int(intial_spot[0])  # gets the row from input
    col_i = coldict[
        intial_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    intial_peice = board[row_i][col_i]  # finds what piece was in the intial spot ex. 'R', 'r', or 'b'
    board[row_i][col_i] = '-'  # replaces the initial spot on the board with with a dash since the peice is being moved
    row_f = int(final_spot[0])  # gets the row from input
    col_f = coldict[
        final_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    board[row_f][col_f] = intial_peice  # changes the final location to a whatever peice was being moved
    return board


def valid_move_red(intial_spot, final_spot):
    # this checks if the user inputted move is valid or not
    row_i = int(intial_spot[0])  # gets the row from user input
    col_i = coldict[
        intial_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    row_f = int(final_spot[0])  # gets the row from user input
    col_f = coldict[
        final_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    intial_peice = board[row_i][col_i]  # finds what piece was in the intial spot ex. 'R', 'r', or 'b'
    final_peice = board[row_f][col_f]  # finds what piece was in the final spot ex. 'R', 'r', or 'b'
    move = 'invalid'  # defaults move to invalid
    jump = 'invalid'  # defaults jump to invalid
    middle_peice = 0  # defaults middle piece to 0
    if (row_i < row_f) and (
            ((col_i + 1) == col_f) or ((col_i - 1) == col_f)):  # red can only move south if it is not a king
        # and only one row to the east or west if it is not jumping
        if intial_peice == 'r' and final_peice == '-':  # if the initial piece is red and final peice is -, it can move
            move = 'valid'  # move is then valid if it makes it here
            jump = 'no'  # since it only move one row and column it didnt jump
    elif (row_i < row_f) and (
            ((col_i + 2) == col_f) or ((col_i - 2) == col_f)):  # red can only move south if it is not a king
        # and only two rows to the east or west if it is jumping
        if col_f - col_i == 2:  # if red is jumping to the east
            middle_peice = board[row_f - 1][col_f - 1]  # the piece it is jumping
            board[row_f - 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if red is jumping to the west
            middle_peice = board[row_f - 1][col_f + 1]  # the piece it is jumping
            board[row_f - 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'r' and final_peice == '-':  # if the initial piece is red and final peice is -
            if middle_peice == 'b' or middle_peice == 'B':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    # if it did not reach the end of any above ifs the move was not valid
    return move, jump


def valid_move_black(intial_spot, final_spot):
    # this checks if the user inputted move is valid or not
    row_i = int(intial_spot[0])  # gets the row from user input
    col_i = coldict[
        intial_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    row_f = int(final_spot[0])  # gets the row from user input
    col_f = coldict[
        final_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    intial_peice = board[row_i][col_i]  # finds what piece was in the intial spot ex. 'R', 'r', or 'b
    final_peice = board[row_f][col_f]  # finds what piece was in the final spot ex. 'R', 'r', or 'b'
    move = 'invalid'  # defaults move to invalid
    jump = 'invalid'  # defaults move to invalid
    middle_peice = 0  # defaults middle piece to 0
    if (row_i > row_f) and (
            ((col_i + 1) == col_f) or ((col_i - 1) == col_f)):  # black can only move north if it is not a king
        # and only one row to the east or west if it is not jumping
        if intial_peice == 'b' and final_peice == '-':  # if the initial piece is black and final peice is -, it can move
            move = 'valid'  # move is then valid if it makes it here
            jump = 'no'  # since it only move one row and column it didnt jump
    elif (row_i > row_f) and (
            ((col_i + 2) == col_f) or ((col_i - 2) == col_f)):  # black can only move north if it is not a king
        # and only two rows to the east or west if it is jumping
        if col_f - col_i == 2:  # if black is jumping to the east
            middle_peice = board[row_f + 1][col_f - 1]  # the piece it is jumping
            board[row_f + 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if black is jumping to the west
            middle_peice = board[row_f + 1][col_f + 1]  # the piece it is jumping
            board[row_f + 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'b' and final_peice == '-':  # if the initial piece is black and final peice is -
            if middle_peice == 'r' or middle_peice == 'R':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    # if it did not reach the end of any above ifs the move was not valid
    return move, jump


def update_kings(board):
    # if a red peice makes it to the south of the board it becomes a king, if a black peice makes it to the north
    # of the board it becomes a king
    top_row = board[0]  # grabs the top row of the board in a list
    bottom_row = board[7]  # grabs the bottom row of the board in a list
    i = 0  # count to iterate through list
    while i <= 7:  # loops 7 times
        if top_row[i] == 'b':  # if a b is in the top row it becomes a king
            top_row[i] = 'B'
        if bottom_row[i] == 'r':  # if a r is in the top row it becomes a king
            bottom_row[i] = 'R'
        i += 1
    board[0] = top_row  # updates the new top row to the board
    board[7] = bottom_row  # updates the new bottom row to the board
    return board


def valid_move_black_king(intial_spot, final_spot):
    # this checks if the user inputted move is valid or not
    row_i = int(intial_spot[0])  # gets the row from user input
    col_i = coldict[
        intial_spot[1]]  # gets the column from input. It is input as a letter and needs to change to a numbe
    row_f = int(final_spot[0])  # gets the row from user input
    col_f = coldict[
        final_spot[1]]  # gets the column from input. It is input as a letter and needs to change to a number
    intial_peice = board[row_i][col_i]  # finds what piece was in the intial spot ex. 'R', 'r', or 'b
    final_peice = board[row_f][col_f]  # finds what piece was in the final spot ex. 'R', 'r', or 'b'
    move = 'invalid'  # defaults move to invalid
    jump = 'invalid'  # defaults move to invalid
    middle_peice = 0  # defaults middle piece to 0
    if ((row_i + 1 == row_f) or (row_i - 1 == row_f)) and (((col_i + 1) == col_f) or ((col_i - 1) == col_f)):
        # black can only move north and south if it is a king and only one row to the east or west if it is not jumping
        if intial_peice == 'B' and final_peice == '-':  # if the initial piece is black and final peice is -, it can move
            move = 'valid'  # move is then valid if it makes it here
            jump = 'no'  # since it only moved one row and column it didnt jump
    elif (row_i - 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        # if black king is moving north and trying to jump
        if col_f - col_i == 2:  # if black is jumping to the east
            middle_peice = board[row_f + 1][col_f - 1]  # the piece it is jumping
            board[row_f + 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if black is jumping to the west
            middle_peice = board[row_f + 1][col_f + 1]  # the piece it is jumping
            board[row_f + 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'B' and final_peice == '-':  # if the initial piece is black and final peice is -
            if middle_peice == 'r' or middle_peice == 'R':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    elif (row_i + 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        # if black king is moving north and trying to jump
        if col_f - col_i == 2:  # if black is jumping to the east
            middle_peice = board[row_f - 1][col_f - 1]  # the piece it is jumping
            board[row_f - 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if black is jumping to the west
            middle_peice = board[row_f - 1][col_f + 1]  # the piece it is jumping
            board[row_f - 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'B' and final_peice == '-':  # if the initial piece is black and final peice is -
            if middle_peice == 'r' or middle_peice == 'R':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    return move, jump


def valid_move_red_king(intial_spot, final_spot):
    # this checks if the user inputted move is valid or not
    row_i = int(intial_spot[0])  # gets the row from user input
    col_i = coldict[
        intial_spot[1]]  # gets the column from input. It is input as a letter and needs to change to a numbe
    row_f = int(final_spot[0])  # gets the row from user input
    col_f = coldict[final_spot[1]]  # gets the column from input. It is input as a letter and needs to change to a numbe
    intial_peice = board[row_i][col_i]  # finds what piece was in the intial spot ex. 'R', 'r', or 'b
    final_peice = board[row_f][col_f]  # finds what piece was in the final spot ex. 'R', 'r', or 'b'
    move = 'invalid'  # defaults move to invalid
    jump = 'invalid'  # defaults move to invalid
    middle_peice = 0  # defaults middle piece to 0
    if ((row_i + 1 == row_f) or (row_i - 1 == row_f)) and (((col_i + 1) == col_f) or ((col_i - 1) == col_f)):
        # red can move north and south if it is a king and only one row to the east or west if it is not jumping
        if intial_peice == 'R' and final_peice == '-':  # if the initial piece is red and final peice is -, it can move
            move = 'valid'  # move is then valid if it makes it here
            jump = 'no'  # since it only move one row and column it didnt jump
    elif (row_i + 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        # if red king is moving north and trying to jump
        if col_f - col_i == 2:  # if red is jumping to the east
            middle_peice = board[row_f - 1][col_f - 1]  # the piece it is jumping
            board[row_f - 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if red is jumping to the west
            middle_peice = board[row_f - 1][col_f + 1]  # the piece it is jumping
            board[row_f - 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'R' and final_peice == '-':  # if the initial piece is red and final peice is -
            if middle_peice == 'b' or middle_peice == 'B':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    elif (row_i - 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        # if red king is moving south and trying to jump
        if col_f - col_i == 2:  # if red is jumping to the east
            middle_peice = board[row_f + 1][col_f - 1]  # the piece it is jumping
            board[row_f + 1][col_f - 1] = '-'  # deleting the piece that was jumped
        elif col_f - col_i == -2:  # if red is jumping to the west
            middle_peice = board[row_f + 1][col_f + 1]  # the piece it is jumping
            board[row_f + 1][col_f + 1] = '-'  # deleting the piece that was jumped
        if intial_peice == 'R' and final_peice == '-':  # if the initial piece is red and final peice is
            if middle_peice == 'b' or middle_peice == 'B':  # the spot it wants to jump is occupied by oppenten
                move = 'valid'  # move is then valid if it makes it here
                jump = 'yes'  # since it moved one two rows and columns it did jump
    return move, jump


def king_or_not(intial_spot):
    # checks the intial_spot the user input to see if it is a king or not
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]

    if board[row_i][col_i] == 'B' or board[row_i][
        col_i] == 'R':  # if the spot has a uppercase letter it returns king as yes
        king = 'yes'
    else:
        king = 'no'
    return king


def check_opponent_has_peice(player, board):
    # checks to see if oppenent has a piece left on the board
    game_over = 'yes'  # defaults game_over to yes
    winner = player  # defaults winner to player
    if player == 1:  # player 1 is the red guys
        for i in range(8):  # loops to check each index
            for j in range(8):  # loops to check each index, need nested loop since have a nested list
                peice = board[i][j]  # if any index has an enemy peice in it the game is not over
                if peice == 'b' or peice == 'B':  # if any index has an enemy peice in it the game is not over
                    game_over = 'no'  # if any index has an enemy peice in it the game is not over
                    winner = 1  # if any index has an enemy peice in it the game is not over
                    break

    elif player == 2:  # player 2 is the black pieces
        for i in range(8):  # loops to check each index
            for j in range(8):  # loops to check each index, need nested loop since have a nested list
                peice = board[i][j]  # if any index has an enemy peice in it the game is not over
                if peice == 'R' or peice == 'r':  # if any index has an enemy peice in it the game is not over
                    game_over = 'no'  # if any index has an enemy peice in it the game is not over
                    winner = 2  # if any index has an enemy peice in it the game is not over
                    break  # if any index has an enemy peice in it the game is not over
    # if it doesnt reach the end of either if statement than the player wins
    return game_over, winner


def check_input_format(intial_spot, final_spot):
    # checks to make sure user input stuff in the right format, if they didn't this lets them try again
    # and not end the whole game
    try:  # trys to assign variables to input
        row_i = int(intial_spot[0])
        col_i = coldict[intial_spot[1]]
        row_f = int(final_spot[0])
        col_f = coldict[final_spot[1]]
    except KeyError:  # if there is an error it will print message and assagin error to 'yes'
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except ValueError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except IndexError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    else:  # if not error, errror is assigned to 'no'
        error = 'no'
    return error


def check_input_format_for_double(final_spot):
    # checks to make sure user input stuff in the right format, if they didn't this lets them try again
    # and not end the whole game
    try:  # tries to assign variables to input
        row_f = int(final_spot[0])
        col_f = coldict[final_spot[1]]
    except KeyError:  # if there is an error it will print message and assagin error to 'yes'
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except ValueError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except IndexError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    else:  # if no error occures, error is assigned to 'no'
        error = 'no'
    return error


def another_jump_available(final_spot, player, board):
    # checks if another jump is available to after jump
    row_f = int(final_spot[0])  # gets the row from user input
    col_f = coldict[
        final_spot[1]]  # gets the colmumn from input. It is input as a letter and needs to change to a number
    try:  # tries these statments, if error occurs another jump is not available
        if player == 1:  # player one is red
            # checks four spaces around the final location to see if any opponents peices are around
            if (board[row_f - 1][col_f - 1] == 'b') or (board[row_f - 1][col_f - 1] == 'B'):
                if board[row_f - 2][col_f - 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail
            elif (board[row_f - 1][col_f + 1] == 'b') or (board[row_f - 1][col_f + 1] == 'B'):
                if board[row_f - 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail
            elif (board[row_f + 1][col_f + 1] == 'b') or (board[row_f + 1][col_f + 1] == 'B'):
                if board[row_f + 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail

            elif (board[row_f + 1][col_f - 1] == 'b') or (board[row_f + 1][col_f - 1] == 'B'):
                if board[row_f - 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail

        elif player == 2:
            if (board[row_f - 1][col_f - 1] == 'r') or (board[row_f - 1][col_f - 1] == 'R'):
                if board[row_f - 2][col_f - 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail
            elif (board[row_f - 1][col_f + 1] == 'r') or (board[row_f - 1][col_f + 1] == 'R'):
                if board[row_f - 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail
            elif (board[row_f + 1][col_f + 1] == 'r') or (board[row_f + 1][col_f + 1] == 'R'):
                if board[row_f + 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail


            elif (board[row_f + 1][col_f - 1] == 'r') or (board[row_f + 1][col_f - 1] == 'R'):
                if board[row_f - 2][col_f + 2] == '-':
                    jump_avail = 'yes'
                    return jump_avail

    except IndexError:
        jump_avail = 'no'
        return jump_avail


# ----------------SETUP-----------------------------------------------------------------
coldict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6,
           'H': 7}  # deffining a dictionary to change A-H to 0-7
board = game_board()  # defining og boarg
print(board)  # printing board to user
game_over = 'no'  # initializing variables to let game begin
turn = 0  # initializing variables to let game begin
error = 'yes'  # initializing variables to let game begin
jump_available = 'no'  # initializing variables to let game begin
# ---------------------GAMEPLAY----------------------------------------------------------------------------
while game_over != 'yes':  # while game is not over
    # -------------------------------PLAYER 1(r,R)----------------------------------------------------------------------
    if turn % 2 == 0:  # player ones turn
        player = 1  # assignning player to 1
        while error == 'yes':  # loops untill the user inputs info in the correct format
            print('Player 1s turn:')
            intial_spot = input(
                'Enter the row (0-7) and the column (A-H) of the piece you want to move seperated by a space').split(
                ' ')
            final_spot = input(
                'Enter the row (0-7) and the column (A-H) of the location you want to move to seperated by a space').split(
                ' ')
            error = check_input_format(intial_spot,
                                       final_spot)  # checks for errors in the input, and returns is yes or no
            print()
        king = king_or_not(intial_spot)  # calling function to check if intial_spot is a king
        if king == 'no':  # if it is not a king
            move, jump = valid_move_red(intial_spot,
                                        final_spot)  # calls regular red move function to check if move was valid
            if move == 'valid' and jump == 'yes':  # if move was valid and a jump happened, board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player,
                                                        board)  # will check if another jump is available

            elif move == 'valid':  # if move was valid but no jump was made board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            else:
                print('Invalid Move')  # if move was not it will go to next players turn
                jump_available = 'no'


        elif king == 'yes':  # if it is a king
            move, jump = valid_move_red_king(intial_spot,
                                             final_spot)  # calls king red move function to check if move was valid
            if move == 'valid' and jump == 'yes':  # if move was valid and a jump happened, board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            elif move == 'valid':  # if move was valid but no jump was made board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)
            else:
                print('Invalid Move')  # if move was not it will go to next players turn
                jump_available = 'no'

        while jump_available == 'yes':  # if another jump is available it will run this loop
            board = update_kings(board)  # first will update board with new kings
            print(board)  # and print board so user can see next jump
            intial_spot = final_spot  # since peice was moved, intial_spot has become final spot
            print('Another jump is available.')
            print("To jump another piece, enter the row(0-7) and column(A-H) you would like to move too separeted by a"
                  "space. If you do not want to jump again enter NO")
            final_spot = input().split()  # getting user input
            if final_spot != ['NO']:  # gives the user the choice to not jump again if they choose
                while error == 'yes':  # checks input to make sure user used valid format
                    error = check_input_format_for_double(final_spot)  # fucntion checks for valid syntax
                    print()
                # since another jump is available it reruns previous code for the move, see next line of comments
                king = king_or_not(intial_spot)
                if king == 'no':
                    move, jump = valid_move_red(intial_spot, final_spot)
                    if move == 'valid' and jump == 'yes':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    elif move == 'valid':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    else:
                        print('Invalid Move')
                        break
                elif king == 'yes':
                    move, jump = valid_move_red_king(intial_spot, final_spot)
                    if move == 'valid' and jump == 'yes':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    elif move == 'valid':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    else:
                        print('Invalid Move')
                jump_available = another_jump_available(final_spot, player, board)
                board = update_kings(board)
                print(board)
            else:
                jump_available = 'no'
                turn += 1  # adds on to the turn counter
            # If another jump is available it will loop back to asking user if they want ot jump or not, once no jump
            # is available it will be next players turn
        print()
    # ---------------------------PLAYER 2(b,B)-----------------------------------------------------------------------------
    else:  # player twos turn
        player = 2
        while error == 'yes':  # loops untill the user inputs info in the correct format
            print('Player 2s turn:')
            intial_spot = input(
                'Enter the row (0-7) and the column (A-H) of the piece you want to move seperated by a space').split(
                ' ')
            final_spot = input(
                'Enter the row (0-7) and the column (A-H) of the location you want to move to seperated by a space').split(
                ' ')
            error = check_input_format(intial_spot,
                                       final_spot)  # checks for errors in the input, and returns is yes or no
            print()

        king = king_or_not(intial_spot)  # calling function to check if intial_spot is a king
        if king == 'no':  # if it is not a king
            move, jump = valid_move_black(intial_spot,
                                          final_spot)  # calls regular black move function to check if move was valid
            if move == 'valid' and jump == 'yes':  # if move was valid and a jump happened, board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player,
                                                        board)  # will check if another jump is available

            elif move == 'valid':  # if move was valid but no jump was made board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player,
                                                        board)  # will check if another jump is available

            else:
                print('Invalid Move')  # if move was not it will go to next players turn
                jump_available = 'no'

        elif king == 'yes':  # if it is a king
            move, jump = valid_move_black_king(intial_spot,
                                               final_spot)  # calls king black move function to check if move was valid
            if move == 'valid' and jump == 'yes':  # if move was valid and a jump happened, board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player,
                                                        board)  # will check if another jump is available

            elif move == 'valid':  # if move was valid but no jump was made board will be updated
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player,
                                                        board)  # will check if another jump is available

            else:
                print('Invalid Move')  # if move was not it will go to next players turn
                jump_available = 'no'

        while jump_available == 'yes':  # if another jump is available it will run this loop
            board = update_kings(board)  # first will update board with new kings
            print(board)  # and print board so user can see next jump
            intial_spot = final_spot  # since peice was moved, intial_spot has become final spot
            print('Another jump is available.')
            print("To jump another piece, enter the row(0-7) and column(A-H) you would like to move too separeted by a"
                  "space. If you do not want to jump again enter N O")
            final_spot = input().split()  # getting user input
            if final_spot != ['NO']:  # gives the user the choice to not jump again if they choose
                while error == 'yes':  # checks input to make sure user used valid format
                    error = check_input_format_for_double(final_spot)  # fucntion checks for valid syntax
                    print()
                king = king_or_not(intial_spot)
                # since another jump is available it reruns previous code for the move, see next line of comments
                if king == 'no':
                    move, jump = valid_move_black(intial_spot, final_spot)
                    if move == 'valid' and jump == 'yes':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    elif move == 'valid':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    else:
                        print('Invalid Move')
                        break
                elif king == 'yes':
                    move, jump = valid_move_black_king(intial_spot, final_spot)
                    if move == 'valid' and jump == 'yes':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    elif move == 'valid':
                        board = update_board_with_player_move(intial_spot, final_spot)
                    else:
                        print('Invalid Move')
                jump_available = another_jump_available(final_spot, player, board)
                board = update_kings(board)
                print(board)
            else:
                jump_available = 'no'
        # If another jump is available it will loop back to asking user if they want ot jump or not, once no jump
        # is available it will be next players turn
        print()
    # --------------UPDATES THAT HAPPEN AFTER EACH TURN-----------------------------------------
    game_over, winner = check_opponent_has_peice(player,
                                                 board)  # check to make sure game is not over after each players turn
    board = update_kings(board)  # updates kings

    print(board)
    error = 'yes'  # resets error so it will loop properly again
# ---------------------GAME OVER------------------------------------------------------
p1_count = 0
p2_count = 0
if winner == 1:
    print('Player 1 Wins!')
    p1_count += 1
elif winner == 2:
    print('PLayer 2 Wins!')
    p2_count += 1
    # HAVE A COUNTER , DO THIS UNTIL THE GAME IS QUIT AND THEN WRITE TO A FILE

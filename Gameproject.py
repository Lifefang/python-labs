import numpy as np
#-------------------SOME WILD FUNCTIONS THAT JUST KEEP GROWING--------------------------------------
def game_board():
    board = [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['r', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'b', '-', 'b', '-', 'R', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'b', '-', 'B', '-', '-'],
        ['-', '-', 'R', '-', '-', '-', 'r', '-'],
        ['-', 'B', '-', 'b', '-', 'b', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
    ]
    board = np.array(board)
    return board

def update_board_with_player_move(intial_spot, final_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]
    intial_peice = board[row_i][col_i]
    board[row_i][col_i] = '-'
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    board[row_f][col_f] = intial_peice
    return board

def valid_move_red(intial_spot, final_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    intial_peice = board[row_i][col_i]
    final_peice = board[row_f][col_f]
    move = 'invalid'
    jump = 'invalid'
    middle_peice = 0
    if (row_i < row_f) and (((col_i+1) == col_f) or ((col_i - 1) == col_f)):
        if intial_peice == 'r' and final_peice == '-':
            move = 'valid'
            jump = 'no'
    elif (row_i < row_f) and (((col_i+2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f-1][col_f-1]
            board[row_f - 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f-1][col_f+1]
            board[row_f - 1][col_f + 1] = '-'
        if intial_peice == 'r' and final_peice == '-':
            if middle_peice == 'b' or middle_peice == 'B':
                move = 'valid'
                jump = 'yes'

    return move, jump

def valid_move_black(intial_spot, final_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    intial_peice = board[row_i][col_i]
    final_peice = board[row_f][col_f]
    move = 'invalid'
    jump = 'invalid'
    middle_peice = 0
    if (row_i > row_f) and (((col_i+1) == col_f) or ((col_i - 1) == col_f)):
        if intial_peice == 'b' and final_peice == '-':
            move = 'valid'
            jump = 'no'
    elif (row_i > row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f + 1][col_f - 1]
            board[row_f + 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f + 1][col_f + 1]
            board[row_f + 1][col_f + 1] = '-'
        if intial_peice == 'b' and final_peice == '-':
            if middle_peice == 'r' or middle_peice == 'R':
                move = 'valid'
                jump = 'yes'
    return move, jump

def update_kings(board):
    top_row = board[0]
    bottom_row = board[7]
    i = 0
    while i <= 7:
        if top_row[i] == 'b':
            top_row[i] = 'B'
        if bottom_row[i] == 'r':
            bottom_row[i] = 'R'
        i += 1
    board[0] = top_row
    board[7] = bottom_row
    return board

def valid_move_black_king(intial_spot, final_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    intial_peice = board[row_i][col_i]
    final_peice = board[row_f][col_f]
    move = 'invalid'
    jump = 'invalid'
    middle_peice = 0
    if ((row_i + 1 == row_f) or(row_i-1 == row_f)) and (((col_i + 1) == col_f) or ((col_i - 1) == col_f)):
        if intial_peice == 'B' and final_peice == '-':
            move = 'valid'
            jump = 'no'
    elif (row_i - 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f + 1][col_f - 1]
            board[row_f + 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f + 1][col_f + 1]
            board[row_f + 1][col_f + 1] = '-'
        if intial_peice == 'B' and final_peice == '-':
            if middle_peice == 'r' or middle_peice == 'R':
                move = 'valid'
                jump = 'yes'
    elif (row_i+2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f-1][col_f-1]
            board[row_f - 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f-1][col_f+1]
            board[row_f - 1][col_f + 1] = '-'
        if intial_peice == 'B' and final_peice == '-':
            if middle_peice == 'r' or middle_peice == 'R':
                move = 'valid'
                jump = 'yes'
    return move, jump

def valid_move_red_king(intial_spot, final_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    intial_peice = board[row_i][col_i]
    final_peice = board[row_f][col_f]
    move = 'invalid'
    jump = 'invalid'
    middle_peice = 0
    if ((row_i + 1 == row_f) or(row_i-1 == row_f)) and (((col_i + 1) == col_f) or ((col_i - 1) == col_f)):
        if intial_peice == 'R' and final_peice == '-':
            move = 'valid'
            jump = 'no'
    elif (row_i + 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f - 1][col_f - 1]
            board[row_f - 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f - 1][col_f + 1]
            board[row_f - 1][col_f + 1] = '-'
        if intial_peice == 'R' and final_peice == '-':
            if middle_peice == 'b' or middle_peice == 'B':
                move = 'valid'
                jump = 'yes'
    elif (row_i - 2 == row_f) and (((col_i + 2) == col_f) or ((col_i - 2) == col_f)):
        if col_f - col_i == 2:
            middle_peice = board[row_f + 1][col_f - 1]
            board[row_f + 1][col_f - 1] = '-'
        elif col_f - col_i == -2:
            middle_peice = board[row_f + 1][col_f + 1]
            board[row_f + 1][col_f + 1] = '-'
        if intial_peice == 'R' and final_peice == '-':
            if middle_peice == 'b' or middle_peice == 'B':
                move = 'valid'
                jump = 'yes'
    return move, jump

def king_or_not(intial_spot):
    row_i = int(intial_spot[0])
    col_i = coldict[intial_spot[1]]

    if board[row_i][col_i] == 'B' or board[row_i][col_i] == 'R':
        king = 'yes'
    else:
        king = 'no'
    return king

def check_opponent_has_peice(player,board):
    game_over = 'yes'
    winner = player
    if player == 1:
        for i in range(8):
            for j in range(8):
                peice = board[i][j]
                if peice == 'b' or peice == 'B':
                    game_over = 'no'
                    winner = 1
                    break

    elif player == 2:
        for i in range(8):
            for j in range(8):
                peice = board[i][j]
                if peice == 'R' or peice == 'r':
                    game_over = 'no'
                    winner = 2
                    break
    return game_over, winner

def check_input_format(intial_spot, final_spot):
    try:
        row_i = int(intial_spot[0])
        col_i = coldict[intial_spot[1]]
        row_f = int(final_spot[0])
        col_f = coldict[final_spot[1]]
    except KeyError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except ValueError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except IndexError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    else:
        error = 'no'
    return error

def check_input_format_for_double(final_spot):
    try:
        row_f = int(final_spot[0])
        col_f = coldict[final_spot[1]]
    except KeyError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except ValueError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    except IndexError:
        print('Check to make sure your input is in the valid format, row (0-7) and column(A-H), EX: 0 B')
        error = 'yes'
    else:
        error = 'no'
    return error

def another_jump_available(final_spot, player, board):
    row_f = int(final_spot[0])
    col_f = coldict[final_spot[1]]
    jump_avail = 'noN'
    try:
        if player == 1:
            if (((board[row_f + 1][col_f + 1] or board[row_f + 1][col_f - 1] or board[row_f - 1][col_f + 1] or
                  board[row_f - 1][col_f - 1]) == 'b') or ((board[row_f + 1][col_f + 1] or board[row_f + 1][
                col_f - 1] or board[row_f - 1][col_f + 1] or board[row_f - 1][col_f - 1]) == 'B')):
                if ((board[row_f + 2][col_f + 2] or board[row_f + 2][col_f - 2] or board[row_f - 2][col_f + 2] or
                  board[row_f - 2][col_f - 2]) == '-'):
                    jump_avail = 'yes'
                    return jump_avail

        elif player == 2:
            if (((board[row_f + 1][col_f + 1] or board[row_f + 1][col_f - 1] or board[row_f - 1][col_f + 1] or
                  board[row_f - 1][col_f - 1]) == 'r') or ((board[row_f + 1][col_f + 1] or board[row_f + 1][
                col_f - 1] or board[row_f - 1][col_f + 1] or board[row_f - 1][col_f - 1]) == 'R')):
                if (board[row_f + 2][col_f + 2] or board[row_f + 2][col_f - 2] or board[row_f - 2][col_f + 2] or
                    board[row_f - 2][col_f - 2]) == '-':
                    jump_avail = 'yes'
                    return jump_avail

    except IndexError:
        jump_avail = 'no'
        return jump_avail

#----------------SETUP-----------------------------------------------------------------
coldict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
board = game_board()
print(board)
game_over = 'no'
turn = 0
error = 'yes'
jump_available = 'no'
#---------------------GAMEPLAY----------------------------------------------------------------------------
while game_over != 'yes':
#-------------------------------PLAYER 1(r,R)----------------------------------------------------------------------
    if turn % 2 == 0:
        player = 1
        while error == 'yes':
            print('Player 1s turn:')
            intial_spot = input('Enter the row (0-7) and the column (A-H) of the piece you want to move seperated by a space').split(' ')
            final_spot = input('Enter the row (0-7) and the column (A-H) of the location you want to move to seperated by a space').split(' ')
            error = check_input_format(intial_spot, final_spot)
            print()
        king = king_or_not(intial_spot)
        if king == 'no':
            move, jump = valid_move_red(intial_spot,final_spot)
            if move == 'valid' and jump == 'yes':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            elif move == 'valid':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            else:
                print('Invalid Move')
                jump_available = 'no'

        elif king == 'yes':
            move, jump = valid_move_red_king(intial_spot, final_spot)
            if move == 'valid' and jump == 'yes':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)
                print(jump_available)
                print(420)
            elif move == 'valid':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)
                print(69)
            else:
                print('Invalid Move')
                jump_available = 'no'
                print(80)

        while jump_available == 'yes':
            board = update_kings(board)
            print(board)
            intial_spot = final_spot
            print('Another jump is available.')
            print("To jump another piece, enter the row(0-7) and column(A-H) you would like to move too separeted by a"
                  "space. If you do not want to jump again enter NO")
            final_spot = input().split()
            if final_spot != ['NO']:
                while error == 'yes':
                    error = check_input_format_for_double(final_spot)
                    print()
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

        print()
#---------------------------PLAYER 2(b,B)-----------------------------------------------------------------------------
    else:
        player = 2
        while error == 'yes':
            print('Player 2s turn:')
            intial_spot = input('Enter the row (0-7) and the column (A-H) of the piece you want to move seperated by a space').split(' ')
            final_spot = input('Enter the row (0-7) and the column (A-H) of the location you want to move to seperated by a space').split(' ')
            error = check_input_format(intial_spot, final_spot)
            print()

        king = king_or_not(intial_spot)
        if king == 'no':
            move, jump = valid_move_black(intial_spot, final_spot)
            if move == 'valid' and jump == 'yes':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            elif move == 'valid':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            else:
                print('Invalid Move')
                jump_available = 'no'

        elif king == 'yes':
            move, jump = valid_move_black_king(intial_spot, final_spot)
            if move == 'valid' and jump == 'yes':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            elif move == 'valid':
                board = update_board_with_player_move(intial_spot, final_spot)
                jump_available = another_jump_available(final_spot, player, board)

            else:
                print('Invalid Move')
                jump_available = 'no'

        while jump_available == 'yes':
            board = update_kings(board)
            print(board)
            intial_spot = final_spot
            print('Another jump is available.')
            print("To jump another piece, enter the row(0-7) and column(A-H) you would like to move too separeted by a"
                  "space. If you do not want to jump again enter N O")
            final_spot = input().split()
            if final_spot != ['NO']:
                while error == 'yes':
                    error = check_input_format_for_double(final_spot)
                    print()
                king = king_or_not(intial_spot)
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
        print()
#--------------UPDATES THAT HAPPEN AFTER EACH TURN-----------------------------------------
    game_over, winner = check_opponent_has_peice(player, board)
    board = update_kings(board)
    turn += 1
    print(board)
    error = 'yes'
#---------------------GAME OVER------------------------------------------------------
if winner == 1:
    print('Player 1 Wins!')
elif winner == 2:
    print('PLayer 2 Wins!')

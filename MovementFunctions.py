def red_moves(row_initial, col_initial):
    if board[row_initial][col_initial] == 'r':
        moves = []
        for row_final_index, row_final in enumerate(board):
            for col_final_index, col_final_string in enumerate(row_final):
                if (row_initial - row_final_index == -1) and (abs(col_initial - col_final_index) == 1) and (
                        col_final_string != '~'):  # clears base criteria
                    if ((col_final_string == 'b') or (col_final_string == 'B')) and (
                            col_initial - col_final_index == 1):  # black to the left of red
                        try:
                            if board[row_final_index + 1][col_final_index - 1] == '.':
                                moves.append(((row_final_index + 1), (col_final_index - 1)))
                                # from this point double jump is considered
                                if (board[row_final_index + 3][col_final_index - 3] == '.') and (
                                        (board[row_final_index + 2][col_final_index - 2] == 'b') or (
                                        board[row_final_index + 2][
                                            col_final_index - 2] == 'B')):  # double jump to the left
                                    moves.append(((row_final_index + 3), (col_final_index - 3)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index + 5][col_final_index - 5] == '.') and (
                                            (board[row_final_index + 4][col_final_index - 4] == 'b') or (
                                            board[row_final_index + 4][
                                                col_final_index - 4] == 'B')):  # triple jump to the left
                                        moves.append(((row_final_index + 5), (col_final_index - 5)))
                                    if (board[row_final_index + 5][col_final_index - 1] == '.') and (
                                            (board[row_final_index + 4][col_final_index - 0] == 'b') or (
                                            board[row_final_index + 4][col_final_index - 0] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index - 1)))
                                if (board[row_final_index + 3][col_final_index + 1] == '.') and (
                                        (board[row_final_index + 2][col_final_index + 0] == 'b') or (
                                        board[row_final_index + 2][
                                            col_final_index + 0] == 'B')):  # double jump to the right
                                    moves.append(((row_final_index + 3), (col_final_index + 1)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index + 5][col_final_index - 1] == '.') and (
                                            (board[row_final_index + 4][col_final_index - 0] == 'b') or (
                                            board[row_final_index + 4][col_final_index - 0] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index - 1)))
                                    if (board[row_final_index + 5][col_final_index + 3] == '.') and (
                                            (board[row_final_index + 4][col_final_index + 2] == 'b') or (
                                            board[row_final_index + 4][col_final_index + 2] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index + 3)))
                            else:
                                continue
                        except:
                            continue
                    elif ((col_final_string == 'b') or (col_final_string == 'B')) and (
                            col_initial - col_final_index == -1):  # black to the right of red
                        try:
                            if board[row_final_index + 1][col_final_index + 1] == '.':
                                moves.append(((row_final_index + 1), (col_final_index + 1)))
                                # from this point double jump is considered 
                                if (board[row_final_index + 3][col_final_index + 3] == '.') and (
                                        (board[row_final_index + 2][col_final_index + 2] == 'b') or (
                                        board[row_final_index + 2][col_final_index + 2] == 'B')):
                                    moves.append(((row_final_index + 3), (col_final_index + 3)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index + 5][col_final_index + 5] == '.') and (
                                            (board[row_final_index + 4][col_final_index + 4] == 'b') or (
                                            board[row_final_index + 4][col_final_index - 4] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index + 5)))
                                    if (board[row_final_index + 5][col_final_index + 1] == '.') and (
                                            (board[row_final_index + 4][col_final_index + 0] == 'b') or (
                                            board[row_final_index + 4][col_final_index + 0] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index + 1)))
                                if (board[row_final_index + 3][col_final_index - 1] == '.') and (
                                        (board[row_final_index + 2][col_final_index - 0] == 'b') or (
                                        board[row_final_index + 2][col_final_index - 0] == 'B')):
                                    moves.append(((row_final_index + 3), (col_final_index - 1)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index + 5][col_final_index + 1] == '.') and (
                                            (board[row_final_index + 4][col_final_index + 0] == 'b') or (
                                            board[row_final_index + 4][col_final_index + 0] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index + 1)))
                                    if (board[row_final_index + 5][col_final_index - 3] == '.') and (
                                            (board[row_final_index + 4][col_final_index - 2] == 'b') or (
                                            board[row_final_index + 4][col_final_index - 2] == 'B')):
                                        moves.append(((row_final_index + 5), (col_final_index - 3)))
                            else:
                                continue
                        except:
                            continue
                    elif (col_final_string == 'r') or (col_final_string == 'R'):  # no moving on fellow red
                        continue
                    else:
                        moves.append((row_final_index, col_final_index))  # empty immediate space
                else:
                    continue

        if moves == []:
            return 'This piece has no possible moves, please choose another piece.'
        else:
            for i in range(len(moves)):
                for n in moves[i]:
                    if n < 0:
                        moves.pop(i)
                        i -= 1
                        break
            return moves

    else:
        return 'Must select a red piece!'


def black_moves(row_initial, col_initial):
    if board[row_initial][col_initial] == 'b':
        moves = []
        for row_final_index, row_final in enumerate(board):
            for col_final_index, col_final_string in enumerate(row_final):
                if (row_initial - row_final_index == 1) and (abs(col_initial - col_final_index) == 1) and (
                        col_final_string != '~'):  # clears base criteria
                    if ((col_final_string == 'r') or (col_final_string == 'R')) and (
                            col_initial - col_final_index == 1):  # red to the left of black
                        try:
                            if board[row_final_index - 1][col_final_index - 1] == '.':
                                moves.append(((row_final_index - 1), (col_final_index - 1)))
                                # from this point double jump is considered
                                if (board[row_final_index - 3][col_final_index - 3] == '.') and (
                                        (board[row_final_index - 2][col_final_index - 2] == 'r') or (
                                        board[row_final_index - 2][
                                            col_final_index - 2] == 'R')):  # double jump to the left
                                    moves.append(((row_final_index - 3), (col_final_index - 3)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index - 5][col_final_index - 5] == '.') and (
                                            (board[row_final_index - 4][col_final_index - 4] == 'r') or (
                                            board[row_final_index - 4][
                                                col_final_index - 4] == 'R')):  # triple jump to the left:
                                        moves.append(((row_final_index - 5), (col_final_index - 5)))
                                    if (board[row_final_index - 5][col_final_index - 1] == '.') and (
                                            (board[row_final_index - 4][col_final_index - 0] == 'r') or (
                                            board[row_final_index + -4][col_final_index - 0] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index - 1)))
                                if (board[row_final_index - 3][col_final_index + 1] == '.') and (
                                        (board[row_final_index - 2][col_final_index - 0] == 'r') or (
                                        board[row_final_index - 2][col_final_index - 0] == 'R')):
                                    moves.append(((row_final_index - 3), (col_final_index + 1)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index - 5][col_final_index - 1] == '.') and (
                                            (board[row_final_index - 4][col_final_index - 0] == 'r') or (
                                            board[row_final_index - 4][col_final_index - 0] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index - 1)))
                                    if (board[row_final_index - 5][col_final_index + 3] == '.') and (
                                            (board[row_final_index - 4][col_final_index + 2] == 'r') or (
                                            board[row_final_index - 4][col_final_index + 2] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index + 3)))
                            else:
                                continue
                        except:
                            continue
                    elif ((col_final_string == 'r') or (col_final_string == 'R')) and (
                            col_initial - col_final_index == -1):  # red to the right of black
                        try:
                            if board[row_final_index - 1][col_final_index + 1] == '.':
                                moves.append(((row_final_index - 1), (col_final_index + 1)))
                                # from this point double jump is considered 
                                if (board[row_final_index - 3][col_final_index + 3] == '.') and (
                                        (board[row_final_index - 2][col_final_index + 2] == 'r') or (
                                        board[row_final_index - 2][col_final_index + 2] == 'R')):
                                    moves.append(((row_final_index - 3), (col_final_index + 3)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index - 5][col_final_index + 5] == '.') and (
                                            (board[row_final_index - 4][col_final_index + 4] == 'r') or (
                                            board[row_final_index - 4][col_final_index + 4] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index + 5)))
                                    if (board[row_final_index - 5][col_final_index + 1] == '.') and (
                                            (board[row_final_index - 4][col_final_index + 0] == 'r') or (
                                            board[row_final_index - 4][col_final_index + 0] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index + 1)))
                                if (board[row_final_index - 3][col_final_index - 1] == '.') and (
                                        (board[row_final_index - 2][col_final_index - 0] == 'r') or (
                                        board[row_final_index - 2][col_final_index - 0] == 'R')):
                                    moves.append(((row_final_index - 3), (col_final_index - 1)))
                                    # from this point triple jump is considered
                                    if (board[row_final_index - 5][col_final_index + 1] == '.') and (
                                            (board[row_final_index - 4][col_final_index + 0] == 'r') or (
                                            board[row_final_index - 4][col_final_index + 0] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index + 1)))
                                    if (board[row_final_index - 5][col_final_index - 3] == '.') and (
                                            (board[row_final_index - 4][col_final_index - 2] == 'r') or (
                                            board[row_final_index - 4][col_final_index - 2] == 'R')):
                                        moves.append(((row_final_index - 5), (col_final_index - 3)))
                            else:
                                continue
                        except:
                            continue
                    elif (col_final_string == 'b') or (col_final_string == 'B'):  # no moving on fellow black
                        continue
                    else:
                        moves.append((row_final_index, col_final_index))  # empty immediate space
                else:
                    continue

        if moves == []:
            return 'This piece has no possible moves, please choose another piece.'
        else:
            for i in range(len(moves)):
                for n in moves[i]:
                    if n < 0:
                        moves.pop(i)
                        i -= 1
                        break
            return moves

    else:
        return 'Must select a black piece!'


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np


def game_board():
    board = [
        ['~', 'r', '~', '.', '~', 'r', '~', 'r'],
        ['r', '~', 'r', '~', 'r', '~', '.', '~'],
        ['~', '.', '~', '.', '~', 'r', '~', 'r'],
        ['.', '~', 'r', '~', '.', '~', '.', '~'],
        ['~', 'r', '~', 'r', '~', '.', '~', '.'],
        ['b', '~', '.', '~', '.', '~', 'b', '~'],
        ['~', 'r', '~', 'b', '~', 'b', '~', 'b'],
        ['b', '~', '.', '~', 'b', '~', '.', '~'],
    ]
    board = np.array(board)
    return board


board = game_board()  # very importaint that you have your list saved as a global list named board, trust me it's easier this way
print(red_moves(3, 2))
print(black_moves(7, 0))

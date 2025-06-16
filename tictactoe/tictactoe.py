"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countx, counto = 0, 0
    for i in board:
        countx += i.count('X')
        counto += i.count('O')

    return 'X' if countx <= counto else 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    x, y = action[0], action[1]

    if not (x in range(0, 3) and y in range(0, 3)) or new_board[x][y] != EMPTY:
        raise Exception
    else:
        new_board[x][y] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for row in board:
        if all(cell == 'X' for cell in row):
            return 'X'
        if all(cell == 'O' for cell in row):
            return 'O'

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 'X'
        if all(board[row][col] == 'O' for row in range(3)):
            return 'O'

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    return 1 if w == 'X' else -1 if w == 'O' else 0


# def minimax(board):
#     """
#     Returns the optimal action for the current player on the board.
#     """
#     if terminal(board):
#         return None

#     def max_value(board):
#         mx = -1000000
#         optimal_move = set()
#         if terminal(board):
#             return utility(board), optimal_move

#         for action in actions(board):
#             temp = min_value(result(board, action))[0]
#             if (temp > mx):
#                 mx = temp
#                 optimal_move = action

#         return mx, optimal_move

#     def min_value(board):
#         mn = 10000000
#         optimal_move = set()
#         if terminal(board):
#             return utility(board), optimal_move

#         for action in actions(board):
#             temp = max_value(result(board, action))[0]
#             if (temp < mn):
#                 mn = temp
#                 optimal_move = action

#         return mn, optimal_move

#     turn = player(board)
#     if (turn == 'X'):
#         return max_value(board)[1]

#     else:
#         return min_value(board)[1]


## Alpha Beta Pruning
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board, alpha, beta):
        mx = -1000000
        optimal_move = set()
        if terminal(board):
            return utility(board), optimal_move

        for action in actions(board):
            temp = min_value(result(board, action), alpha, beta)[0]
            if (temp > mx):
                mx = temp
                optimal_move = action
            alpha = max(alpha, mx)
            if( beta<= alpha):
                break

        return mx, optimal_move

    def min_value(board, alpha, beta):
        mn = 10000000
        optimal_move = set()
        if terminal(board):
            return utility(board), optimal_move

        for action in actions(board):
            temp = max_value(result(board, action), alpha, beta)[0]
            if (temp < mn):
                mn = temp
                optimal_move = action
            beta = min(mn, beta)
            if( beta<= alpha):
                break

        return mn, optimal_move

    turn = player(board)
    if (turn == 'X'):
        return max_value(board, float("-inf"), float("inf"))[1]

    else:
        return min_value(board, float("-inf"), float("inf"))[1]

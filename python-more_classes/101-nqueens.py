#!/usr/bin/python3

""" nqueens solution second iteration"""

def queen_in_diag(matrix, N, pos_x, pos_y):

    """ returns 1 if a queen (true value) is in the diagonal """

    UPPER_BOUND = N
    LOWER_BOUND = 0

    for i in range(UPPER_BOUND):

        """ check in the +- (backward) diagonal for queens """

        if pos_x - i >= LOWER_BOUND and pos_y - i >= LOWER_BOUND:
            if not matrix[pos_x - i][pos_y - i] == 0:
                return 1

        """ check in the +- (forward) diagonal for queens """
        if pos_x + i < UPPER_BOUND and pos_y + i < UPPER_BOUND:
            if not matrix[pos_x + i][pos_y + i] == 0:
                return 1

        """ check in the ++ diagonal (forward) for queens """
        if pos_x + i < UPPER_BOUND and pos_y - i >= LOWER_BOUND:
            if not matrix[pos_x + i][pos_y - i] == 0:
                return 1

        """" check in the ++ diagonal (backward) for queens """
        
        if pos_x - i >= LOWER_BOUND and pos_y + i < UPPER_BOUND:
            if not matrix[pos_x - i][pos_y + i] == 0:
                return 1
    return 0

##############################################################

def queen_in_row(matrix, pos_x):

    """ returns 1 if there is a queen in the row """

    if 1 in matrix[pos_x]:
        return 1
    return 0

###############################################################

def queen_in_vert(matrix, N, pos_y):

    """ returns 1 if there is a queen in the column """

    UPPER_BOUND = N

    for i in range(UPPER_BOUND):
        if not matrix[i][pos_y] == 0:
            return 1
    return 0

#################################################################

if __name__ == "__main__":

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = int(sys.argv[1]) + 1

    if N <= 4:
        print("N must be at least 4")
        exit(1)

    board = []
    board_row = []
    for i in range(N):
        for j in range (N):
            board_row.append(0)
        board.append(board_row)
        board_row = []

    print(board)
    
    possible_answer = []
    possible_answer_row = []
    queens_in_answer = 0

    for iters in range(int(len(board) / 2) + 1):
        for i in range(iters, len(board)):
            for j in range(len(board[i])):
                if (queen_in_diag(board, N, i, j) == 0 and
                    queen_in_vert(board, N, j) == 0 and
                    queen_in_row(board, i) == 0):
                    print(queen)
        

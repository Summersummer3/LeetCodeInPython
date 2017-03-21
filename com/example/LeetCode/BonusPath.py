# -*- coding: utf-8 -*-
# __author__ = 'summer'

def bonusPath(board):
    """
    :param board: square matrix[n][n]
    :return: path and final bonus
    """
    bonus = 0
    path = []
    pathMtr = []

    w = len(board)
    v = len(board[0])

    for k in xrange(w):
        tmp = []
        for l in xrange(len(board[k])):
            tmp.append(0)
        pathMtr.append(tmp)

    for i in xrange(w):
        for j in xrange(len(board[i])):
            if not i and not j:
                continue
            elif not i and j:
                board[i][j] = board[i][j] + board[i][j - 1]
            elif not j and i:
                board[i][j] = board[i][j] + board[i - 1][j]
                pathMtr[i][j] = 1
            else:
                if board[i - 1][j] > board[i][j - 1]:
                    board[i][j] = board[i][j] + board[i - 1][j]
                    pathMtr[i][j] = 1
                else:
                    board[i][j] = board[i][j] + board[i][j - 1]

    # terminal position
    w = w - 1
    v = v - 1

    while w or v:
        path.append((w, v))
        bonus += board[w][v]
        if pathMtr[w][v]:
            w -= 1
        else:
            v -= 1
    # start point position
    path.append((0, 0))

    return board[len(board) - 1][len(board[0]) - 1], path


print bonusPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
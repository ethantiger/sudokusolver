import math

board1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board2 = [[3, 0, 0, 0, 4, 0, 0, 8, 6],
        [6, 4, 0, 3, 0, 0, 5, 1, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 0],
        [0, 8, 3, 0, 1, 0, 0, 4, 0],
        [0, 9, 0, 0, 0, 7, 0, 0, 2],
        [9, 0, 7, 0, 6, 0, 0, 0, 0],
        [0, 3, 4, 5, 7, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 9, 0, 0, 3]]

def print_board(board):
    col_count = 0
    row_count = 0
    for row in board:
        if row_count % 3 == 0:
            print("------------------------")
        row_count += 1
        s = ""
        for item in row:
            if col_count % 3 == 0:
                s += "| "
            col_count += 1
            if item == 0:
                s += "  "
            else:
                s += (str(item) + " ")
            if col_count == 9:
                s += "|"
                col_count = 0
        print(s)
    print("------------------------")

def find_zero(board):
    row_count = -1
    col_count = -1
    point = []
    for row in board:
        row_count += 1
        for item in row:
            col_count += 1
            if item == 0:
                point.append(row_count)
                point.append(col_count - row_count * 9)
                return point
    return None

def is_valid(board, row, col, value):
    # Check Horizontal
    for item in board[row]:
        if item == value:
            return False

    # Check Vertical
    for rows in board:
        if rows[col] == value:
            return False

    # Check Family
    row_idx = math.floor(row / 3)
    col_idx = math.floor(col / 3)
    if row_idx == 1:
        row_idx = 3
    elif row_idx == 2:
        row_idx = 6
    if col_idx == 1:
        col_idx = 3
    elif col_idx == 2:
        col_idx = 6
    for i in range(row_idx, row_idx + 3):
        for j in range(col_idx, col_idx + 3):
            if board[i][j] == value:
                return False
    return True


def solve(board):
    # Base Case
    if find_zero(board) == None:
        return board

    # Recursive Case
    empty_cell = find_zero(board)
    # Try 1
    if is_valid(board, empty_cell[0], empty_cell[1], 1):
        board[empty_cell[0]][empty_cell[1]] = 1
        try_1 = solve(board)
        if try_1 is not None:
            return try_1

    # Try 2
    if is_valid(board, empty_cell[0], empty_cell[1], 2):
        board[empty_cell[0]][empty_cell[1]] = 2
        try_2 = solve(board)
        if try_2 is not None:
            return try_2

    # Try 3
    if is_valid(board, empty_cell[0], empty_cell[1], 3):
        board[empty_cell[0]][empty_cell[1]] = 3
        try_3 = solve(board)
        if try_3 is not None:
            return try_3

    # Try 4
    if is_valid(board, empty_cell[0], empty_cell[1], 4):
        board[empty_cell[0]][empty_cell[1]] = 4
        try_4 = solve(board)
        if try_4 is not None:
            return try_4

    # Try 5
    if is_valid(board, empty_cell[0], empty_cell[1], 5):
        board[empty_cell[0]][empty_cell[1]] = 5
        try_5 = solve(board)
        if try_5 is not None:
            return try_5

    # Try 6
    if is_valid(board, empty_cell[0], empty_cell[1], 6):
        board[empty_cell[0]][empty_cell[1]] = 6
        try_6 = solve(board)
        if try_6 is not None:
            return try_6

    # Try 7
    if is_valid(board, empty_cell[0], empty_cell[1], 7):
        board[empty_cell[0]][empty_cell[1]] = 7
        try_7 = solve(board)
        if try_7 is not None:
            return try_7

    # Try 8
    if is_valid(board, empty_cell[0], empty_cell[1], 8):
        board[empty_cell[0]][empty_cell[1]] = 8
        try_8 = solve(board)
        if try_8 is not None:
            return try_8

    # Try 9
    if is_valid(board, empty_cell[0], empty_cell[1], 9):
        board[empty_cell[0]][empty_cell[1]] = 9
        try_9 = solve(board)
        if try_9 is not None:
            return try_9

    # Nothing Works
    board[empty_cell[0]][empty_cell[1]] = 0
    return None

print_board(solve('Put your board here'))
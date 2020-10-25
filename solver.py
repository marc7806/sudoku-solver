board = [
    [0, 0, 5, 0, 0, 0, 1, 0, 0],
    [0, 6, 1, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 3, 8, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 3, 0, 0, 0, 9],
    [0, 1, 3, 5, 0, 0, 0, 0, 2],
    [9, 0, 0, 0, 0, 2, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [4, 0, 0, 0, 5, 9, 0, 0, 3]
]


def print_board(bo):
    for i in range(len(bo)):
        if i != 0 and i % 3 == 0:
            print('- - - - - - - - - - - ')

        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')

            if j == len(bo[i]) - 1:
                print(bo[i][j])
            else:
                print(bo[i][j], end=' ')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                # return row and column
                return i, j
    return None


def check_row(bo, idx, num):
    for i in range(len(bo[idx])):
        if bo[idx][i] == num:
            return False
    return True


def check_col(bo, idx, num):
    for i in range(len(bo)):
        if bo[i][idx] == num:
            return False
    return True


def check_box(bo, num, pos):
    row = pos[0] // 3  # integer division
    col = pos[1] // 3  # integer division

    row_start = row * 3
    row_end = (row + 1) * 3

    col_start = col * 3
    col_end = (col + 1) * 3

    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if bo[i][j] == num:
                return False
    return True


def valid(bo, num, pos):
    # check horizontal
    if check_row(bo, pos[0], num):
        # check vertical
        if check_col(bo, pos[1], num):
            # check the box
            if check_box(bo, num, pos):
                return True
    return False


# solves a sudoku board using backtrack algorithm
def solve(bo):
    empty = find_empty(bo)

    # recursion base case
    if not empty:
        return True
    else:
        row, col = empty

        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i

                if solve(bo):
                    return True
                else:
                    bo[row][col] = 0
        return False


print('Starting to solve board: ')
print_board(board)
print('=========================')
solve(board)
print_board(board)

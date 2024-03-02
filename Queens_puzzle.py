def is_safe(board, row, col, n):  # check if it is safe to put queen into part of the board or not
    # Check if there is a queen in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):  # solve_n_queens_util
    # if col number is out of the boards range, the board is completed correctly and return true
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            # call the solve_n_queen_util function again and pass the next column to it
            if solve_n_queens_util(board, col + 1, n):
                return True
            # if the progam cannot put queen in any of rows in next column, make the current columns queen to 0
            # and then for loops continue and put the queen in other rows of this column
            board[i][col] = 0
    # if the program cannot put queen in any rows of this column , return false
    return False


def solve_n_queens(n):  # solving function
    # creating board
    board = [[0 for _ in range(n)] for _ in range(n)]
    # call solve_n_queens_util function
    solve_n_queens_util(board, 0, n)
    # returning the board
    return board


def print_board(board):  # print_board function
    for row in board:
        print(row)


# get the length of the board from the user
n = int(input("Enter the length of the board: "))
# call solve_n_solution and pass the "n" to it, and put the return board to  "solution"
solution = solve_n_queens(n)
# call print _board function and pass the board to it
print_board(solution)
# get the user info before closing the program
input()

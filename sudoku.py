from pprint import pprint
 
def nextEmpty(board):
    # finds the next row, column on the board that is equal to 0, which is an empty square
    # return row, column tuple or (None, None) if there is no empty square
 
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
 
    return None, None
 
def isValid(board, guess, row, column):
    # figures out whether the guess at the row/column of the board is a valid guess
    # returns True or False
 
    # checking the row
    rowValues = board[row]
    if guess in rowValues:
        return False
 
    # checking the column
    columnValues = [board[i][column] for i in range(9)]
    if guess in columnValues:
        return False
 
    # checking 3x3 square
    rowStart = (row // 3) * 3
    columnStart = (column // 3) * 3
 
    for r in range(rowStart, rowStart + 3):
        for c in range(columnStart, columnStart + 3):
            if board[r][c] == guess:
                return False
 
    return True
 
def solve(board):
    # solve sudoku using backtracking
    # the board is a list of lists, where each inner list is a row in our sudoku board
    # with a value of 0 representing a blank square
    # return whether a solution exists
    # mutates board to be the solution (if solution exists)
   
    # find first empty square
    row, column = nextEmpty(board)
 
    # checks if nextEmpty returned None; None - meaning that the sudoku board is filled/solved
    if row is None:
        return True
   
    # make a guess for the next empty square
    for guess in range(1, 10):
        # check if the guess works
        if isValid(board, guess, row, column):
            # if valid set the square
            board[row][column] = guess
            # recursively call the solver again to find next guess
            if solve(board):
                return True
       
        # if the guess isn't valid we reset the square to 0
        board[row][column] = 0
 
    # if none of the guesses 1-9 work, the board is unsolvable so return False
    return False
 
if __name__ == '__main__':
    exampleBoard = [
        [0, 0, 0,  8, 0, 0,   4, 2, 0],
        [5, 0, 0,  6, 7, 0,   0, 0, 0],
        [0, 0, 0,  0, 0, 9,   0, 0, 5],
 
        [7, 4, 0,  1, 0, 0,   0, 0, 0],
        [0, 0, 9,  0, 3, 0,   7, 0, 0],
        [0, 0, 0,  0, 0, 7,   0, 4, 8],
 
        [8, 0, 0,  4, 0, 0,   0, 0, 0],
        [0, 0, 0,  0, 9, 8,   0, 0, 3],
        [0, 9, 5,  0, 0, 3,   0, 0, 0]
    ]
    pprint(exampleBoard)
    print(solve(exampleBoard))
    pprint(exampleBoard)

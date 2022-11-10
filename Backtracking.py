class backtracking:
    board_grid = {}
    board = []
    '''
    constructor which initializes the board range which AC-3 solved 

    input: board_grid dictionary with the results of AC-3, board is
    the locations of each tile

    output: none
    '''
    def __init__(self, board_grid, board) -> None:
        self.board_grid = board_grid
        self.board = board
        pass
    """
    checking the validity of the item which is to be inserted 
    in said position.

    input: sudoku_grid is the 9*9 grid array, int row position,
    int column position, int value to be inserted.

    output: boolean validity of the item
    """
    def isValid(self, sudoku_grid, row, col, item):
        row_valid = item not in sudoku_grid[row] #check the row for duplicates
        col_valid = True #assume valid for column until not
        for i in range(0,9):
            if item == sudoku_grid[i][col]:
                col_valid = False
        box_valid = True #assume valid for box until not
        for i in range(row//3*3,row//3*3+3):
            for j in range(col//3*3,col//3*3+3):
                if item == sudoku_grid[i][j]:
                    box_valid = False
        return row_valid and col_valid and box_valid
    '''
    This is to recursivley implement the back tracking algorithm

    input: Array sudoku 9*9 grid, int number of row, int number of col
    
    output: boolean True for solved and False for not
    '''
    def process(self, sudoku_grid, row=0, col=0):
        if row == 9:
            return True #end
        elif col == 9:
            return self.process(sudoku_grid, row+1, 0) #end col move to next row
        elif sudoku_grid[row][col] != 0:
            return self.process(sudoku_grid, row, col+1)
        else:
            range_val = self.board_grid[self.board[row][col]]
            for item in range_val.domain: #check for each element 1 - 9
                if self.isValid(sudoku_grid, row, col, item): 
                    #if valid then save value and proceed to solve subsequent squares
                    sudoku_grid[row][col] = item
                    if self.process(sudoku_grid, row, col+1):
                        return sudoku_grid
                    #if no valid item left with that config then backtrack and start over. 
                    sudoku_grid[row][col] = 0
            return False

    
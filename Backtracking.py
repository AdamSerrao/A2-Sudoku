class backtracking:
    """
    checking the validity of the item which is to be inserted 
    in said position.

    input: sodoku_grid is the 9*9 grid array, int row position,
    int column position, int value to be inserted.

    output: boolean validity of the item
    """
    def isValid(self, sodoku_grid, row, col, item):
        row_valid = item not in sodoku_grid[row] #check the row for duplicates
        col_valid = True #assume valid for column until not
        for i in range(0,9):
            if item == sodoku_grid[i][col]:
                col_valid = False
        box_valid = True #assume valid for box until not
        for i in range(row//3*3,row//3*3+3):
            for j in range(col//3*3,col//3*3+3):
                if item == sodoku_grid[i][j]:
                    box_valid = False
        return row_valid and col_valid and box_valid
    '''
    This is to recursivley implement the back tracking algorithm

    input: Array sodoku 9*9 gird, int number of row, int number of col
    
    output: boolean True for solved and False for not
    '''
    def process(self, sodoku_grid, row=0, col=0):
        if row == 9:
            return True #end
        elif col == 9:
            return self.process(sodoku_grid, row+1, 0) #end col move to next row
        elif sodoku_grid[row][col] != 0:
            return self.process(sodoku_grid, row, col+1)
        else:
            for item in range(1,10): #check for each element 1 - 9
                if self.isValid(sodoku_grid, row, col, item): 
                    #if valid then save value and proceed to solve subsequent squares
                    sodoku_grid[row][col] = item
                    if self.process(sodoku_grid, row, col+1):
                        return sodoku_grid
                    #if no valid item left with that config then backtrack and start over. 
                    sodoku_grid[row][col] = 0
            return False

    
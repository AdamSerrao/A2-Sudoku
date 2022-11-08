"""
Assignment 2 Sudoku


Group 8
Filip Kossowski
Harshul Mehta
Neek Panchal
Adam Serrao
"""
from Backtracking import backtracking
#Classes

class Queue:
    def __init__ (self):
        self.list = []

    def insert(self,value):
        self.list.append(value)
        return

    def remove(self):
        value = self.list[0]
        self.list = self.list[1:]
        return value

    def __iter__(self):
        return iter(self.list)

    def __str__(self):
        return str(self.list)

    def size(self):
        return len(self.list)

class Node:
    """Node refers to each cell on the board the 
    class is implemented to make it easier to track 
    the different domains of each cell as we progress 
    through out the AC-3 alogorithm"""
    
    def __init__ (self,value = None):
        self.domain = [1,2,3,4,5,6,7,8,9]
        self.value = value
        self.neighbors = []

    def set_neighbors(self,loc,board):
        letter = loc[0]
        num = int(loc[1])
        
        #Horizontal and Vertical Neighbors
        for i in board:
            for j in i:
                if(j[0] == letter or int(j[1]) == num):
                    if(j != loc):
                        self.neighbors.append(j)

        #Box Neighbors

        box = find_box(letter,num)
        let_low = letters.index(box[0][0])
        let_high = letters.index(box[1][0])
        num_low = int(box[0][1])
        num_high = int(box[1][1])

        for i in range(let_low,let_high+1):
            for j in range(num_low,num_high+1):
                value = letters[i]+str(j)
                if(value not in self.neighbors and value != loc):
                    self.neighbors.append(value)
        return

    def __str__ (self):
        return f"Value: {self.value} Domain: {self.domain}"

    def set_value(self,value):
        self.value = value
        self.domain = [int(value)]
        return

    def shrink_domain(self,value):
        if value in self.domain:
            self.domain.remove(value)

        if len(self.domain) == 1:
            self.value = self.domain[0]
        return
    
#Global Variables
board_dict = {}
letters = ['A','B','C','D','E','F','G','H','I']
size = 9
constraints = Queue()


#Functions
def display_grid(grid):
    
    space = 0
    for i in range(0,9):
        
        space2 = 0
        for j in range(0,9):
            if(grid[i][j] != None):
                print(grid[i][j], end = " ")
            else:
                print("#", end = " ")
            space2 += 1
            if(space2 == 3):
                print(" ",end="")
                space2 = 0
        space += 1
        if(space == 3):
            print()
            space = 0
        print()
    return
def display_board():
    
    space = 0
    for i in board:
        
        space2 = 0
        for j in i:
            if(board_dict[j].value != None):
                print(board_dict[j].value, end = " ")
            else:
                print("#", end = " ")
            space2 += 1
            if(space2 == 3):
                print(" ",end="")
                space2 = 0
        space += 1
        if(space == 3):
            print()
            space = 0
        print()
    return
def change_dict_to_arr():
    grid = [ [0] * 9 for _ in range(9)]
    row,col = 0,0
    for i in board:
        for j in i:
            if(board_dict[j].value != None):
                #append to array
                grid[row][col] = board_dict[j].value
            col = col + 1
        col = 0
        row = row + 1
    return grid

def generate_board():
    #initializes a Board for iteration and the dixtionary for each cell
    board = []

    for i in letters:
        row = []
        for j in range(size):
            row.append(i+str(j+1))
            board_dict[i+str(j+1)] = Node()
        board.append(row)

    for k in board_dict:
        board_dict[k].set_neighbors(k,board)

    return board

def find_box(letter,num):
    #A function that return the range of each box
    if(letter < 'D'):
        if(num < 4):
            box = ("A1","C3")
        elif(num < 7):
            box = ("A4","C6")
        else:
            box = ("A7","C9")

    elif(letter < 'G'):
        if(num < 4):
            box = ("D1","F3")
        elif(num < 7):
            box = ("D4","F6")
        else:
            box = ("D7","F9")

    else:
        if(num < 4):
            box = ("G1","I3")
        elif(num < 7):
            box = ("G4","I6")
        else:
            box = ("G7","I9")

    return box

def constraint_generator(cell, board):
    letter = cell[0]
    num = int(cell[1])
    
    #Horizontal and Vertical Constraints
    for i in board:
        for j in i:
            if(j[0] == letter or int(j[1]) == num):
                if((cell,j) not in constraints and (j,cell) not in constraints and cell != j):
                    constraints.insert((cell,j))
    #Box Constraints
    #uses find_box to determine which box to check(get the range of the box) 
    box = find_box(letter,num)
    let_low = letters.index(box[0][0])
    let_high = letters.index(box[1][0])
    num_low = int(box[0][1])
    num_high = int(box[1][1])

    for i in range(let_low,let_high+1):
        for j in range(num_low,num_high+1):
            value = letters[i]+str(j)
            if((cell,value) not in constraints and (value,cell) not in constraints and cell != value):
                constraints.insert((cell,value))
    return

def initialize_board(input_values):
    size =len(input_values)
    for i in range(size):
        for j in range(size):
            if(input_values[i][j] != ''):
                board_dict[letters[i]+str(j+1)].set_value(int(input_values[i][j]))

def AC3():
    queue = constraints

    while queue.size() > 0:
        arc = queue.remove()
        #Take values from arc 
        xi = board_dict[arc[0]]
        xj = board_dict[arc[1]]
        #Make the values arc consistent
        if(revise(xi,xj)):
            #if values cannot be made arc consisitent the algorithm failed
            if(len(xi.domain) == 0):
                return False
            #add all neighbors to queue
            for xk in xi.neighbors:
                
                if(xk != xj and (xk,arc[0]) not in queue ):
                    queue.insert((xk,arc[0]))

                    if( (arc[0],xk) not in queue):
                        queue.insert((arc[0],xk))
    #Checks that the board is solved
    for i in board_dict:
        
        if(board_dict[i].value == None):
            return change_dict_to_arr()

    return True

def revise(xi,xj):
    revised = False
    for x in xi.domain:
        valid = False
        for y in xj.domain:
            if (y != x):
                valid = True
        if(not valid):
            xi.shrink_domain(x)
            revised = True
        #print(xi.domain)

    return revised



#Main

f = open("Input_Hard.txt",'r')

start_val = []

#preprocess data from file
for i in f:
    line = i.strip()
    line = line[2:]
    start_val.append(line.split(','))
    
board = generate_board()

#generate constraints
for i in board:
    for j in i:
        constraint_generator(j, board)

#fill board with values from file
initialize_board(start_val)

#display board before AC-3
print("Initial Board: ")
display_board()

solved = AC3()
 
#display board after AC-3
print("---------------------------------------")
if solved == True:
    print("Solution: ")
    print()
    display_board()
else:
    print("Failed to solve with AC-3")
    print("Stopped at: ")
    print()
    display_board()
    print("---------------------------------------")
    algo = backtracking()
    back_board = algo.process(solved)
    print("Solved with Backtracking:")
    print()
    display_grid(back_board)









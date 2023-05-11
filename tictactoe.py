import random




# Variables
matrix = [['', '', ''], ['', '', ''], ['', '', '']]
symbols = ['X', 'O']
player_one = []
player_two = []
n = 1

# Randomly choosing symbol for player
player_one_symbol = symbols[random.randint(0, 1)]
player_one.append(player_one_symbol)

print("Player 1 uses", player_one[0])

if player_one_symbol == symbols[0]:
    print("Player 2 uses O")
    player_two = [symbols[1]]
else:
    print("Player 2 uses X")
    player_two = [symbols[0]]




# Funciton to print the matrix
def print_matrix():
    for i in matrix:
        print(i, '\n')


played_boxes = []

# Entering player input in the matrix 
def insert_symbol(value): 
    n = len(value) - 1
    if str(value[n]) in played_boxes:
        print("found it to be duplicate")
        # ------------------- Fix the function and then write algo to find win or lose conditions --------
        return 0
    played_boxes.append(value[n]) 
    row = (int(value[n]) - 1) // 3
    column = (int(value[n]) - 1) % 3
    # print("current row column value is ", row, column, value[n], value, n)
    matrix[row][column] = value[0]

# Getting input from Players symbol and matrix position
for i in range(0,9):
    X = input("Player one where to ? ")
    player_one.append(X)
    insert_symbol(player_one)
    print_matrix()
    X = input("Player Two where to ? ")
    player_two.append(X)
    insert_symbol(player_two)
    print_matrix()

    
    






# Algo to check winner




# Announcing winner or draw


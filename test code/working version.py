# defs
file_path = '/Users/giovanni.votano/Desktop/Connect four/matchdata.txt'
def read_data(file_path): 
    with open(file_path, 'r') as f:
        data = f.read()
        games = data.strip().split('\n\n')
        return(games)
    

def create_board():
    board = [[ '' for i in range(7)] for i in range(6)]
    return board

def place_piece(board, move):
    player = move[0]
    column = int(move[1])-1

    for row in range(5, -1, -1):
        if board[row][column] == '':
            board[row][column] = player
            break

def horizontal_win(board):
    for row in board:
        for col in range(len(row) -3):
             if row[col] != '' and row[col] == row[ col+ 1] == row[ col+ 2] == row[ col+ 3]:# first has to check cell is not empty as it can interpret four empty cells as a win
                return True  # You can return True if a horizontal win is found                 return(print(row))
    return False

def vertical_win(board): # add to the row and not the col
    for row in range(len(board)-3):
        for col in range(7):
             if board[row][col] != '' and board[row][col] == board[row +1 ][col] == board[row + 2][col] == board[row +3][col]:# first has to check cell is not empty as it can interpret four empty cells as a win
                return True  # You can return True if a horizontal win is found                 return(print(row))
    return False


# read in example data
game_1 = ['R2','B5','R7','B6','R1','B4','R6','B7','R7','B4','R3','B3','R1','B6','R4','B2','R1','B7','R5','B2','R5','B2','R2','B1','R3','B6','R5','B7','R5','B4','R4','B3','R4','B1','R7','B6','R2','B1','R3','B5','R6','B3']
moves_string = "R3,B6,R2,B3,R3,B7,R5,B7,R4,B1,R6,B5,R5,B4,R1,B3,R2,B2,R3,B2,R6,B1,R4,B5,R7,B4,R5,B7,R7,B1,R1,B2,R4,B6,R1,B3,R6,B4,R2,B6,R7,B5"
game_2 = moves_string.split(',')
moves_string = "R2,B5,R2,B2,R1,B4,R5,B7,R3,B5,R5,B7,R5,B2,R4,B1,R1,B4,R7,B2,R4,B3,R3,B1,R6,B5,R7,B4,R6,B3,R4,B6,R5,B2,R1,B1,R1,B5,R2,B7,R6,B6"
game_3 = moves_string.split(',')
games = [game_1, game_2, game_3]


# apply moves to game board
winner = [] 
for game in games:  # Assuming 'games' is a list of moves for each game
    board = create_board()
    
    for move in game:
        place_piece(board, move)  # Pass the board to the place_piece function
        
        if vertical_win(board):
            winner.append(move)
            print(board)
            break
        if horizontal_win(board):  
            winner.append(move) 
            print(board)
            break
        

print(board) 
print(winner)

# defs
#file_path = '/Users/giovanni.votano/Desktop/Connect four/matchdata.txt'
def read_data(file_path): 
    with open(file_path, 'r') as f:
        data = f.read()
        return(data)

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
        for i in range(len(row) -3):
            if row[i] == row[ i+ 1] == row[ i+ 2] == row[ i+ 3]:
                return True  # You can return True if a horizontal win is found                 return(print(row))
    return False



# apply moves to game board
game_1 = ['R2','B5','R7','B6','R1','B4','R6','B7','R7','B4','R3','B3','R1','B6','R4','B2','R1','B7','R5','B2','R5','B2','R2','B1','R3','B6','R5','B7','R5','B4','R4','B3','R4','B1','R7','B6','R2','B1','R3','B5','R6','B3']
game_2 = ['R2','B5','R7','B6','R1','B4','R6','B7','R7','B4','R3','B3','R1','B6','R4','B2','R1','B7','R5','B2','R5','B2','R2','B1','R3','B6','R5','B7','R5','B4','R4','B3','R4','B1','R7','B6','R2','B1','R3','B5','R6','B3']
games_list = [game_1, game_2]

winner = [] # Initialize a list to store winners
for game in games_list:  # Assuming 'games' is a list of moves for each game
    board = create_board()
    
    for move in game:
        place_piece(board, move)  # Pass the board to the place_piece function
        
        if horizontal_win(board):  # Check for a horizontal win
            winner.append(move)  # Append the winning game to the 'winner' list
            break

print(board) 
print(winner)

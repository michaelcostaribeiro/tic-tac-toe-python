#tic-tac-toe

board = [[board_column+board_row for board_column in range(1,4)] for board_row in range(0, 9, 3)]
ready = ""
winner = False

def show_board():
    print("[COLUMN]  [ 1 ][ 2 ][ 3 ]")
    row = 0
    for board_row in board:
        row +=1
        print("[ROW:", row, end="]     ")
        for element in board_row:
            print("[", element , "]", end="")        
        print()

def winner():
    for row in board:
        if row[0] == row[1] == row[2]:
            print("Player: ", row[0], " wins!")
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            print("Player: ", board[0][col], " wins!")
            return True
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[2][2] == board[2][0]:
            print("Player: ", board[2][2], " wins!")
            return True
    else:
        return False
    
def player_move_X():
    print()
    show_board()
    print()
    column = int(input("Say a number for the column you wanna play: "))
    row = int(input("Now say a number for the row you wanna play: "))
    if board[row-1][column-1] != ("O") or board[row-1][column-1] != ("X"):
        board[row-1][column-1] = str("X")
    else:
        print("This move is invalid, try again.")
        player_move_X()
    winner()

def player_move_O():
    print()
    show_board()
    print()
    column = int(input("Say a number for the column you wanna play: "))
    row = int(input("Now say a number for the row you wanna play: "))
    if board[row-1][column-1] != ("O") or board[row-1][column-1] != ("X"):
        board[row-1][column-1] = str("O")
    else:
        print("This move is invalid, try again.")
        player_move_O()
    winner()

print("Welcome to your tic-tac-toe game")


while not winner:
    player_move_X()
    player_move_O()
    winner = winner()

show_board()












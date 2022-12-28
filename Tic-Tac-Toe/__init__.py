import random


# create the gameboard
def create_gameboard(size):
    gameboard = []
    for row in range(size):
        row_list = []
        for col in range(size):
            row_list.append("-")
        gameboard.append(row_list)

    return gameboard


# print the gameboard
def print_gameboard(gameboard):
    print("The Game Board state ----")
    for row in gameboard:
        row_str = ""
        for col in row:
            row_str += col + " "
        print(row_str)


# check for a win
def check_win(gameboard):
    size = len(gameboard)
    # check for horizontal wins
    for row in gameboard:
        symbol = row[0]
        win = True
        for col in range(1, size):
            if row[col] != symbol or symbol == "-":
                win = False
                break
        if win == True:
            return symbol

    # check for vertical wins
    for col in range(size):
        symbol = gameboard[0][col]
        win = True
        for row in range(1, size):
            if gameboard[row][col] != symbol or symbol == "-":
                win = False
                break
        if win == True:
            return symbol

    # check for diagonal wins
    symbol = gameboard[0][0]
    win = True
    for i in range(1, size):
        if gameboard[i][i + 1] != symbol or symbol == "-":
            win = False
            break
    if win == True:
        return symbol

    symbol = gameboard[0][size - 1]
    win = True
    for i in range(1, size):
        if gameboard[i][size - 1 - i] != symbol or symbol == "-":
            win = False
            break
    if win == True:
        return symbol


# get user input
def get_user_input():
    global row, col
    valid_input = False
    while not valid_input:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if row in range(size) and col in range(size):
                valid_input = True
            else:
                print("Invalid input. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
    return row, col


# computer AI
def get_computer_move(gameboard):
    global row, col
    valid_move = False
    while not valid_move:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if gameboard[row][col] == "-":
            valid_move = True
    return row, col


# place symbol on gameboard
def place_symbol(gameboard, row, col, symbol):
    gameboard[row][col] = symbol


# main game loop
print("Welcome to Tic-Tac-Toe!")
size = int(input("Enter the size of the gameboard: "))
gameboard = create_gameboard(size)

# set up players
player1_symbol = input("Player 1: Do you want to be X or O? ").upper()
if player1_symbol == "X":
    player2_symbol = "O"
else:
    player2_symbol = "X"

# set up the turn order
turn = random.randint(1, 2)
if turn == 1:
    print("Player 1 goes first")
    current_player = 1
    current_symbol = player1_symbol
else:
    print("Computer goes first")
    current_player = 2
    current_symbol = player2_symbol

# game loop
game_over = False
while not game_over:
    # print gameboard
    print_gameboard(gameboard)
    # get move
    if current_player == 1:
        row, col = get_user_input()
    else:
        row, col = get_computer_move(gameboard)
    # place symbol
    place_symbol(gameboard, row, col, current_symbol)
    # check for win
    winner = check_win(gameboard)
    if winner is not None:
        print_gameboard(gameboard)
        if winner == player1_symbol:
            print("Player 1 wins!")
        else:
            print("Computer wins!")
        game_over = True
    # switch turn
    if current_player == 1:
        current_player = 2
        current_symbol = player2_symbol
    else:
        current_player = 1
        current_symbol = player1_symbol

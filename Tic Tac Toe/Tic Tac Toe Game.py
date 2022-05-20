# What do we require in this game
# A board
# Play Game (function)
# Handles turn
# Check win (function)
    # Check rows
    # Check columns
    # Check diagonals
# Check tie (function)
# Flip turn (function)


def check_win():    # Checking for a winner at a time, either for player 1 or 2
    global winner
    global current_player
    global game_not_over
    if current_player == 1:
        if (game_board[0] == "x") and (game_board[1] == "x") and (game_board[2] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[3] == "x") and (game_board[4] == "x") and (game_board[5] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[6] == "x") and (game_board[7] == "x") and (game_board[8] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[0] == "x") and (game_board[3] == "x") and (game_board[6] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[1] == "x") and (game_board[4] == "x") and (game_board[7] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[2] == "x") and (game_board[5] == "x") and (game_board[8] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[0] == "x") and (game_board[4] == "x") and (game_board[8] == "x"):
            winner = "x"
            game_not_over = False
        elif (game_board[2] == "x") and (game_board[4] == "x") and (game_board[6] == "x"):
            winner = "x"
            game_not_over = False
    elif current_player == 2:
        if (game_board[0] == "o") and (game_board[1] == "o") and (game_board[2] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[3] == "o") and (game_board[4] == "o") and (game_board[5] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[6] == "o") and (game_board[7] == "o") and (game_board[8] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[0] == "o") and (game_board[3] == "o") and (game_board[6] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[1] == "o") and (game_board[4] == "o") and (game_board[7] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[2] == "o") and (game_board[5] == "o") and (game_board[8] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[0] == "o") and (game_board[4] == "o") and (game_board[8] == "o"):
            winner = "o"
            game_not_over = False
        elif (game_board[2] == "o") and (game_board[4] == "o") and (game_board[6] == "o"):
            winner = "o"
            game_not_over = False


def check_tie():    # Checking for a tie between the players
    global tie_value
    for item in game_board:     # Iterate all the items from the board (Lists)
        if item != "-":
            tie_value = True    # If all cell is not empty (all filled with x or o), then game is over
        else:
            tie_value = False   # If an empty cell is detected, that means game is not over
            break


def check_game_over():  # To check whether the game is over or not
    global tie_value
    global game_not_over
    global winner
    check_win()
    if game_not_over:   # Here, we will not check the tie if a winner has been declared.
        check_tie()
        if tie_value:   # if tie value is true, then game is over and it is a tie
            game_not_over = False
            winner = "-"


def flip_turn():
    global current_player
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1


def handle_turn(player): # To handles each players' turn
    if player == 1:
        print("\nPLAYER 1")
        position = int(input("Choose a position from 1-9 (except the ones which are filled): "))
        position = position - 1
        if game_board[position] != "x" and game_board[position] != "o":
            game_board[position] = "x"
            display_board()
        else:
            handle_turn(current_player)
    elif player == 2:
        print("\nPLAYER 2")
        position = int(input("Choose a position from 1-9 (except the ones which are filled): "))
        position = position - 1
        if game_board[position] != "o" and game_board[position] != "x":
            game_board[position] = "o"
            display_board()
        else:
            handle_turn(current_player)


def display_board():    # To display the game board
    print(f'{game_board[0]} | {game_board[1]} | {game_board[2]}')
    print(f'{game_board[3]} | {game_board[4]} | {game_board[5]}')
    print(f'{game_board[6]} | {game_board[7]} | {game_board[8]}')
    print("\n")


def play_game():    # This funtion is the starting of all game
    print("The board is displayed below")
    display_board()
    print("\nRULES\nFor Player 1, the symbol is 'x'")
    print("For Player 2, the symbol is 'o'\n")
    while game_not_over:
        handle_turn(current_player)
        check_game_over()
        flip_turn()
    print(Final_result.get(winner))


game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-",]
game_not_over = True
tie_value = False
current_player = 1
winner = ""
Final_result = {"x": "Player 1 has won!", "o": "Player 2 has won!", "-": "The Game is a tie"}
print("WELCOME TO TIC TAC TOE GAME\n")
play_game()


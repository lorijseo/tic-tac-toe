import random


def show_board():
    r1_board = " ".join(board[0])
    r2_board = " ".join(board[1])
    r3_board = " ".join(board[2])
    print(f"{r1_board}\n{r2_board}\n{r3_board}")


def player_x_turn():
    show_board()
    print(f"It's {player_x}'s turn!")
    row_column = input("Write (row,column): ")
    if len(row_column) != 5:
        print("Incorrect coordinates. Try again!")
        player_x_turn()
    elif "(" not in row_column or ")" not in row_column:
        print("Open and close parenthesis when inputting coordinates. Try again!")
        player_x_turn()
    elif "," not in row_column:
        print("Include a comma to separate row and column with a comma. Try again!")
        player_x_turn()
    elif int(row_column[1]) > 4 and int(row_column[3]) > 4:
        print("Coordinates are incorrect. Remember: there are 3 rows and 3 columns. Try again!")
        player_x_turn()
    elif row_column in check_repeats:
        print("That space is already taken. Try again!")
        player_x_turn()
    else:
        check_repeats.append(row_column)
        row = int(row_column[1])
        column = int(row_column[3])
        board[row - 1][column - 1] = "[X]"


def player_o_turn():
    show_board()
    print(f"It's {player_o}'s turn!")
    row_column = input("Write (row,column): ")
    if len(row_column) != 5:
        print("Incorrect coordinates. Try again!")
        player_o_turn()
    elif "(" not in row_column or ")" not in row_column:
        print("Open and close parenthesis when inputting coordinates. Try again!")
        player_o_turn()
    elif "," not in row_column:
        print("Include a comma to separate row and column with a comma. Try again!")
        player_o_turn()
    elif int(row_column[1]) > 4 and int(row_column[3]) > 4:
        print("Coordinates are incorrect. Remember: there are 3 rows and 3 columns. Try again!")
        player_o_turn()
    elif row_column in check_repeats:
        print("That space is already taken. Try again!")
        player_o_turn()
    else:
        check_repeats.append(row_column)
        row = int(row_column[1])
        column = int(row_column[3])
        board[row - 1][column - 1] = "[O]"


def check_row_win(row_num):
    row_x_count = 0
    row_o_count = 0
    for space in row_num:
        if space == "[X]":
            row_x_count += 1
        elif space == "[O]":
            row_o_count += 1
    if row_x_count == 3:
        show_board()
        print(f"{player_x} wins!")
        return "win"
    elif row_o_count == 3:
        show_board()
        print(f"{player_o}wins!")
        return "win"


def check_col_win(col_num):
    col_x_count = 0
    col_o_count = 0
    for index in range(3):
        if board[index][col_num-1] == "[X]":
            col_x_count += 1
        elif board[index][col_num-1] == "[O]":
            col_o_count += 1
    if col_x_count == 3:
        show_board()
        print(f"{player_x} wins!")
        return "win"
    elif col_o_count == 3:
        show_board()
        print(f"{player_o} wins!")
        return "win"


def check_diagonal():
    x_count = 0
    o_count = 0
    if board[0][2] == "[X]" and board[1][1] == "[X]" and board[2][0] == "[X]":
        show_board()
        print(f"{player_x} wins!")
        return "win"
    elif board[0][2] == "[O]" and board[1][1] == "[O]" and board[2][0] == "[O]":
        show_board()
        print(f"{player_o} wins!")
        return "win"
    else:
        for index in range(3):
            if board[index][index] == "[X]":
                x_count += 1
            elif board[index][index] == "[O]":
                o_count += 1
        if x_count == 3:
            show_board()
            print(f"{player_x} wins!")
            return "win"
        elif o_count == 3:
            show_board()
            print(f"{player_o} wins!")
            return "win"


def check_full_board():
    count = 0
    for row in range(0, 3):
        for col in range(0, 3):
            if " " not in board[row][col]:
                count += 1
    if count == 9:
        print("It's a Draw!")
        return "draw"


game = True

players = []
check_repeats = []
r1 = []
r2 = []
r3 = []
for section in range(3):
    r1.append("[ ]")
    r2.append("[ ]")
    r3.append("[ ]")
board = [r1, r2, r3]

print("Welcome to tic-tac-toe!\nLet's determine who goes first!")
player_1 = input("Player1's name: ").upper()
players.append(player_1)
player_2 = input("Player2's name: ").upper()
players.append(player_2)
player_x = random.choice(players)
players.remove(player_x)
player_o = players[0]
print(f"{player_x} will go first using X. {player_o} will go second using O\n")

while game:
    if check_row_win(r1) == "win" or check_row_win(r2) == "win" or check_row_win(r3) == "win" or \
            check_col_win(1) == "win" or check_col_win(2) == "win" or check_col_win(3) == "win" or \
            check_diagonal() == "win" or check_full_board() == "draw":
        print("Game over!")
        break
    else:
        check_full_board()
        for each_row in board:
            check_row_win(each_row)
        for each_col in range(1, 4):
            check_col_win(each_col)
        check_diagonal()
        player_x_turn()

    if check_row_win(r1) == "win" or check_row_win(r2) == "win" or check_row_win(r3) == "win" or \
            check_col_win(1) == "win" or check_col_win(2) == "win" or check_col_win(3) == "win" or \
            check_diagonal() == "win" or check_full_board() == "draw":
        print("Game over!")
        break
    else:
        check_full_board()
        for each_row in board:
            check_row_win(each_row)
        for each_col in range(1, 4):
            check_col_win(each_col)
        check_diagonal()
        player_o_turn()

import random
game = True

r1 = []
r2 = []
r3 = []
for section in range(3):
    r1.append("[ ]")
    r2.append("[ ]")
    r3.append("[ ]")
board = [r1, r2, r3]

check_repeats = []


def show_board():
    r1_board = " ".join(board[0])
    r2_board = " ".join(board[1])
    r3_board = " ".join(board[2])
    print(f"{r1_board}\n{r2_board}\n{r3_board}")


def player_x_turn():
    show_board()
    print("It's Player X's turn!")
    row_column = input("Write (row,column): ")
    if row_column not in check_repeats:
        check_repeats.append(row_column)
        row_column = row_column.replace("(", "")
        row_column = row_column.replace(")", "")
        row_column = row_column.replace(",", "")
        row = int(row_column[0])
        column = int(row_column[1])
        if row > 0 and row < 4 and column > 0 and column < 4:
            board[row - 1][column - 1] = "[X]"
        else:
            print("The coordinates do not exist on the board. Try again!")
            player_x_turn()
    else:
        print("That space is already taken. Try again!")
        player_x_turn()


def player_o_turn():
    show_board()
    print("It's Player O's turn!")
    row_column = input("Write (row,column): ")
    if row_column not in check_repeats:
        check_repeats.append(row_column)
        row_column = row_column.replace("(", "")
        row_column = row_column.replace(")", "")
        row_column = row_column.replace(",", "")
        row = int(row_column[0])
        column = int(row_column[1])
        if row > 0 and row < 4 and column > 0 and column < 4:
            board[row - 1][column - 1] = "[O]"
        else:
            print("The coordinates do not exist on the board. Try again!")
            player_o_turn()
    else:
        print("That space is already taken. Try again!")
        player_o_turn()


players = ["Player X", "Player O"]
# player_1 = random.choice(players)
# players.remove(player_1)
# player_2 = players[0]
player_x = players[0]
player_o = players[1]


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
        print("Player X wins!")
        return 888
    elif row_o_count == 3:
        show_board()
        print("Player O wins!")
        return 888


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
        print("Player X wins!")
        return 888
    elif col_o_count == 3:
        show_board()
        print("Player O wins!")
        return 888


def check_diagonal_1():
    x_count = 0
    o_count = 0
    for index in range(3):
        if board[index][index] == "[X]":
            x_count += 1
        elif board[index][index] == "[O]":
            o_count += 1
    if x_count == 3:
        show_board()
        print("Player X wins!")
        return 888
    elif o_count == 3:
        show_board()
        print("Player O wins!")
        return 888


def check_diagonal_2():
    if board[0][2] == "[X]" and board[1][1] == "[X]" and board[2][0] == "[X]":
        show_board()
        print("Player X wins!")
        return 888
    elif board[0][2] == "[O]" and board[1][1] == "[O]" and board[2][0] == "[O]":
        show_board()
        print("Player O wins!")
        return 888


while game:
    if check_row_win(r1) == 888 or check_row_win(r2) == 888 or check_row_win(r3) == 888 or check_col_win(1) == 888 or \
            check_col_win(2) == 888 or check_col_win(3) == 888 or check_diagonal_1() == 888 or check_diagonal_2() == 888:
        print("Game over!")
        break
    else:
        check_row_win(r1)
        check_row_win(r2)
        check_row_win(r3)
        check_col_win(1)
        check_col_win(2)
        check_col_win(3)
        check_diagonal_1()
        check_diagonal_2()
        player_x_turn()

    if check_row_win(r1) == 888 or check_row_win(r2) == 888 or check_row_win(r3) == 888 or check_col_win(1) == 888 or \
            check_col_win(2) == 888 or check_col_win(3) == 888 or check_diagonal_1() == 888 or check_diagonal_2() == 888:
        print("Game over!")
        break
    else:
        check_row_win(r1)
        check_row_win(r2)
        check_row_win(r3)
        check_col_win(1)
        check_col_win(2)
        check_col_win(3)
        check_diagonal_1()
        check_diagonal_2()
        player_o_turn()

# refactor functions
# randomize player
# choose player name

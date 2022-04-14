# tic tac toe game
# create a board with 3 rows of lists with square brackets
# function to ask to place a marker
# if win when consecutive x (columns or rows are same + 2 different diagonals)
# else draw when no blanks


# create nested list to help call out index

r1 = []
r2 = []
r3 = []
for space in range(3):
    r1.append("[ ]")
    r2.append("[ ]")
    r3.append("[ ]")
board = [r1, r2, r3]

# create visual board for better user interface
board1 = ""
board2 = ""
board3 = ""
for space in range(3):
    board1 += r1[space]
    board2 += r2[space]
    board3 += r3[space]
print(f"{board1}\n{board2}\n{board3}")


# print(r1[0]+r1[1]+r1[2])
# print(r2[0]+r2[1]+r2[2])
# print(r3[0]+r3[1]+r3[2])
#
# print(board[1][1])










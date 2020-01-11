board = [
    ["V","i","n","h"],
    ["i","n","h"," "],
    ["n","h"," "," "],
    ["h"," "," "," "]
]

def check(board, row, col, string, count):
    if row < len(board) and col < len(board[0]) and row >= 0 and col >= 0 and board[row][col] == string[count]:
        return True

def adventure(board, row, col, string, steps, move_list):
    board[0][0] = " "
    move_row = [0, 0, 1,-1]
    move_col = [1,-1, 0, 0]
    for i in range(4):
        if steps == len(string):
            steps = 1
        new_row = row + move_row[i]
        new_col = col + move_col[i]
        if check(board, new_row, new_col, string, steps):
            move_list.append((new_row,new_col))
            board[new_row][new_col] = " "
            adventure(board, new_row, new_col, string, steps+1, move_list)
            board[new_row][new_col] = string[steps]
            move_list.remove((new_row,new_col))
    if len(move_list) == 4:
        print(move_list)

adventure(board, 0, 0, "Vinh", 1, [(0, 0)])
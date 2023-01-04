def is_in_range(n_row, n_col, n):
    if 0 <= n_row < n and 0 <= n_col < n:
        return True
    return False


n = 8

board = []

for _ in range(n):
    board.append(input().split())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "right_up": (-1, 1),
    "left_up": (-1, -1),
    "right_down": (1, 1),
    "left_down": (1, -1),
}

queens = []

for row in range(n):
    for col in range(n):
        if board[row][col] == "K":
            for direction in directions:
                new_row = row + directions[direction][0]
                new_col = col + directions[direction][1]
                while is_in_range(new_row, new_col, n):
                    if board[new_row][new_col] == "Q":
                        queens.append([new_row, new_col])
                        break
                    new_row += directions[direction][0]
                    new_col += directions[direction][1]


if queens:
    [print(queen) for queen in queens]
else:
    print("The king is safe!")
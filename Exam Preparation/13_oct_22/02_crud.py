def is_in_range(n_row, n_col, n):
    if 0 <= n_row < n and 0 <= n_col < n:
        return True
    return False


n = 6

matrix = []

for _ in range(n):
    matrix.append([x for x in input().split()])

position = input()
row = int(position[1])
col = int(position[4])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

line = input()

while line != "Stop":
    data = line.split(", ")
    command, direction = data[0], data[1]
    if direction in directions:
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]
        if is_in_range(next_row, next_col, n):
            if command == "Create":
                value = data[2]
                if matrix[next_row][next_col] == ".":
                    matrix[next_row][next_col] = value
            if command == "Update":
                value = data[2]
                if matrix[next_row][next_col] != ".":
                    matrix[next_row][next_col] = value

            if command == "Delete":
                if matrix[next_row][next_col] != ".":
                    matrix[next_row][next_col] = "."

            if command == "Read":
                if matrix[next_row][next_col] != ".":
                    print(matrix[next_row][next_col])
            row = row + directions[direction][0]
            col = col + directions[direction][1]

    line = input()

for current_row in matrix:
    print(" ".join(current_row))



# ----------------------Second way--------------------------
# n = 6
#
# matrix = []
#
# for _ in range(n):
#     matrix.append([x for x in input().split()])
#
# position = input()
# row = int(position[1])
# col = int(position[4])
#
# line = input()
#
# while line != "Stop":
#     data = line.split(", ")
#     command, direction = data[0], data[1]
#
#     if direction == "up":
#         row = -1
#     if direction == "down":
#         row += 1
#     if direction == "left":
#         col -= 1
#     if direction == "right":
#         col += 1
#
#     if command == "Create":
#         value = data[2]
#         if matrix[row][col] == ".":
#             matrix[row][col] = value
#
#     if command == "Update":
#         value = data[2]
#         if matrix[row][col] != ".":
#             matrix[row][col] = value
#
#     if command == "Delete":
#         if matrix[row][col] != ".":
#             matrix[row][col] = "."
#     if command == "Read":
#         if matrix[row][col] != ".":
#             print(matrix[row][col])
#
#     line = input()
#
# for current_row in matrix:
#     print(" ".join(current_row))
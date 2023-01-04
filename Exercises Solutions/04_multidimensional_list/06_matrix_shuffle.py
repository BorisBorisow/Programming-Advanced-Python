def invalid_indexes(row, col, rows, cols):
    return row < 0 or row >= rows or col < 0 or col >= cols


rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break

    data = command.split()

    if data[0] != "swap" or len(data) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in data[1:]]

    if invalid_indexes(row1, col1, rows, cols) or invalid_indexes(row2, col2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row)

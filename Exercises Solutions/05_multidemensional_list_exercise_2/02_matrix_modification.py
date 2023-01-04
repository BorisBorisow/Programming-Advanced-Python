n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

while True:
    data = input().split()
    command = data[0]
    if command == "END":
        break

    row, col, value = [int(x) for x in data[1:]]

    if row < 0 or col < 0 or row >= n or col >= n:
        print("Invalid coordinates")
        continue

    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for current_row in matrix:
    print(*current_row, sep=" ")




def is_in_range(n_row, n_col, n):
    if 0 <= n_row < n and 0 <= n_col < n:
        return True
    return False


size = int(input())
car_number = input()

car_pos = [0, 0]
distance = 0
matrix = []
t_positions = []


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if "T" in line:
        t_positions.append([row, line.index("T")])

while True:
    command = input()
    if command == "End":
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {car_number} DNF.")
        print(f"Distance covered {distance} km.")
        break

    if command in directions:
        car_pos[0] = car_pos[0] + directions[command][0]
        car_pos[1] = car_pos[1] + directions[command][1]
        if is_in_range(car_pos[0], car_pos[1], size):
            if matrix[car_pos[0]][car_pos[1]] == "F":
                matrix[car_pos[0]][car_pos[1]] = "C"
                distance += 10
                print(f"Racing car {car_number} finished the stage!")
                print(f"Distance covered {distance} km.")
                break
            if matrix[car_pos[0]][car_pos[1]] == "T":
                distance += 30
                matrix[car_pos[0]][car_pos[1]] = "."
                t_positions.remove([car_pos[0], car_pos[1]])
                car_pos[0] = t_positions[0][0]
                car_pos[1] = t_positions[0][1]
                t_positions.remove([car_pos[0], car_pos[1]])
                matrix[car_pos[0]][car_pos[1]] = "."
            else:
                distance += 10

[print(''.join(row)) for row in matrix]
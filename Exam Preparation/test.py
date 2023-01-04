import math


def valid_indexes(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def is_number(el):
    try:
        int(el)
    except ValueError:
        return False


SIZE = 7
player_1, player_2 = input().split(", ")
points = {player_1: 501, player_2: 501}

player_turns = {0: player_2, 1: player_1}
turns_count = 1

matrix = [[x for x in input().split()] for _ in range(SIZE)]

while True:
    r, c = [int(x) for x in input().strip("()").split(", ")]

    if valid_indexes(r, c, SIZE):
        number = is_number(matrix[r][c])
        if number:
            points[player_turns[turns_count % 2]] -= number
        current_points = sum([
            int(matrix[0][c]),
            int(matrix[-1][c]),
            int(matrix[r][0]),
            int(matrix[r][-1])
        ])

        if matrix[r][c] == "D":
            points[player_turns[turns_count % 2]] -= current_points * 2
        if matrix[r][c] == "T":
            points[player_turns[turns_count % 2]] -= current_points * 3
        if matrix[r][c] == "B":
            print(f"{player_turns[turns_count % 2]} won the game with {math.ceil(turns_count / 2)} throws!")
            exit(0)

        if 0 >= points[player_1] or 0 >= points[player_2]:
            break

    turns_count += 1

print(f"{player_turns[turns_count % 2]} won the game with {math.ceil(turns_count / 2)} throws!")

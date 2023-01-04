SIZE = 8

board = []
w_pos = []
b_pos = []
move = 0

positions_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}

positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

for row in range(SIZE):
    line = input().split()
    if "w" in line:
        w_pos = [row, line.index("w")]
    if "b" in line:
        b_pos = [row, line.index("b")]

while w_pos and b_pos:
    move += 1
    if move % 2 != 0:
        while w_pos[0] > 0:
            w_attack_left = [(w_pos[0] - 1), (w_pos[1] - 1)]
            w_attack_right = [(w_pos[0] - 1), (w_pos[1] + 1)]
            if w_attack_left == b_pos or w_attack_right == b_pos:
                position = positions_col[b_pos[1]] + positions_row[b_pos[0]]
                print(f"Game over! White win, capture on {position}.")
                b_pos.clear()
                break
            w_pos[0] -= 1
        else:
            position = positions_col[w_pos[1]] + positions_row[w_pos[0]]
            print(f"Game over! White pawn is promoted to a queen at {position}.")
            b_pos.clear()
            break
    elif move % 2 == 0:
        while b_pos[0] < SIZE - 1:
            b_attack_left = [(w_pos[0] + 1), (w_pos[1] - 1)]
            b_attack_right = [(w_pos[0] + 1), (w_pos[1] + 1)]
            if b_attack_left == w_pos or b_attack_right == w_pos:
                position = positions_col[w_pos[1]] + positions_row[w_pos[0]]
                print(f"Game over! White win, capture on {position}.")
                w_pos.clear()
                break
            b_pos[0] += 1
        else:
            position = positions_col[b_pos[1]] + positions_row[b_pos[0]]
            print(f"Game over! White pawn is promoted to a queen at {position}.")
            w_pos.clear()
            break

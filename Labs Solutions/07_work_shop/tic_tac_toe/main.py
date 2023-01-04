def print_initial_board_position():
    print("This is the numeration of the board:")
    print("| 1 | 2 | 3")
    print("| 4 | 5 | 6")
    print("| 7 | 8 | 9")


def setup():
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    player_1_sign = input(f"{player_1}, choose your sign (X or 0): ").upper()
    while not player_1_sign in ["X", "O"]:
        player_1_sign = input(f"{player_1}, choose your sign (X or 0): ").upper()
    player_2_sign = "0" if player_1_sign == "X" else "X"
    print(f"{player_1} starts ")
if __name__ = "__main__":
    setup()
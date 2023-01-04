players = input().split(", ")
matrix = [input().split() for _ in range(6)]
player_resting = {player: 0 for player in players}

while True:
    row, col = [int(x) for x in input().strip("()").split(", ")]

    position = matrix[row][col]

    if player_resting[players[0]]:
        player_resting[players[0]] -= 1
        players[0], players[1] = players[1], players[0]
        continue

    if position == "E":
        print(f"{players[0]} found the Exit and wins the game!")
        break
    if position == "T":
        print(f"{players[0]} is out of the game! The winner is {players[1]}.")
        break
    if position == "W":
        player_resting[players[0]] += 1
        print(f"{players[0]} hits a wall and needs to rest.")

    players[0], players[1] = players[1], players[0]
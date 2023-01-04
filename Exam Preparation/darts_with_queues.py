from collections import deque


def create_board():
    matrix = [[x for x in input().split()] for _ in range(7)]
    return matrix


def is_valid(row, col):
    if 0 <= row < 7 and 0 <= col < 7:
        return True
    False


def triple_score(row):
    points = int(board[row][0]) + int(board[row][-1]) + int(board[0][row]) + int(board[-1][row])
    return points * 3


def double_score(row):
    points = int(board[row][0]) + int(board[row][-1]) + int(board[0][row]) + int(board[-1][row])
    return points * 2


players = deque(input().split(", "))
scores = deque([501, 501])
board = create_board()
turns = deque([0, 0])

while True:
    dart = tuple(input().split(", "))
    r = int(dart[0][-1])
    c = int(dart[1][0])
    element = None
    player = players.popleft()
    score = scores.popleft()
    turn = turns.popleft()
    turn += 1
    if is_valid(r, c):
        element = board[r][c]
    if element:
        if element == "D":
            score -= double_score(r)
        elif element == "T":
            score -= triple_score(r)
        elif element == "B":
            break
        else:
            score -= int(element)

    if score <= 0:
        break
    players.append(player)
    scores.append(score)
    turns.append(turn)

print(f"{player} won the game with {turn} throws!")

size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - idx - 1])

primary_sum = sum(primary)
secondary_sum = sum(secondary)

print(abs(primary_sum - secondary_sum))
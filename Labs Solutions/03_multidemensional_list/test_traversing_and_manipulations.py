def matrix_
ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mm = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]

# print(ll[4])
# print(mm[1])
# print(mm[1][3])
# print(mm[-1])
# print(mm[-1][-1])

n = len(mm)
m = len(mm[0])

for row_index in range(n):
    print(mm[row_index])
    for column_index in range(m):
        print(mm[row_index][column_index], end=" ")
        print()
n, m = [int(x) for x in input().split(", ")]  # 3, 6

matrix = []
matrix_sum = 0
for _ in range(n):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)

# def read_matrix():
#     n, m = [int(x) for x in input().split(", ")]  # 3, 6
#
#     print(n, m)
#
#     matrix = []
#
#     for _ in range(n):
#         row = [int(x) for x in input().split(", ")]
#         matrix.append(row)
#     return matrix
#
# matrix = read_matrix()
# print(matrix)
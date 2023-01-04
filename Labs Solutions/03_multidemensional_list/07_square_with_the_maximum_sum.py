# import sys
# from io import StringIO
#
# test1 = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
#
# """
#
# test2 = """2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
#
# """
#
# sys.stdin = StringIO(test1)
# # sys.stdin = StringIO(test2)
#
# rows_count, columns_count = [int(x) for x in input().split(", ")]
#
# matrix = []
# sums = []
#
# for _ in range(rows_count):
#     row = [int(x) for x in input().split(", ")]
#     matrix.append(row)
#
# for r in range(rows_count - 1):
#     for c in range(columns_count - 1):
#         current_sum = matrix[r][c] + \
#             matrix[r][c+1] + \
#             matrix[r + 1][c] + \
#             matrix[r + 1][c + 1]
#         sums.append((
#             current_sum,
#             r,
#             c
#         ))
# print(sums)

rows, cols = [int(x) for x in input().split(",")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = -999999999999999
max_sub_matrix = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        sub_matrix = [
            matrix[row_index][col_index],
            matrix[row_index][col_index + 1],
            matrix[row_index + 1][col_index],
            matrix[row_index + 1][col_index + 1],
        ]
        current_sum = sum(sub_matrix)
        if max_sum < current_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()


print(" ".join(map(str, max_sub_matrix[:2])))
print(" ".join(map(str, max_sub_matrix[2:])))
# print(max_sub_matrix[0], max_sub_matrix[1])
# print(max_sub_matrix[2], max_sub_matrix[3])
print(max_sum)


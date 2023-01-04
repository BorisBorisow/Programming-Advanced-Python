rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = -99999999999
max_sub_matrix = 0

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        sub_matrix = [
            matrix[row_index][col_index],
            matrix[row_index][col_index + 1],
            matrix[row_index][col_index + 2],
            matrix[row_index + 1][col_index],
            matrix[row_index + 1][col_index + 1],
            matrix[row_index + 1][col_index + 2],
            matrix[row_index + 2][col_index],
            matrix[row_index + 2][col_index + 1],
            matrix[row_index + 2][col_index + 2],
        ]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")
print(max_sub_matrix[0], max_sub_matrix[1], max_sub_matrix[2])
print(max_sub_matrix[3], max_sub_matrix[4], max_sub_matrix[5])
print(max_sub_matrix[6], max_sub_matrix[7], max_sub_matrix[8])

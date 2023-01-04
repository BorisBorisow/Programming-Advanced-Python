# import sys
# from io import StringIO
#
# test_input1 = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
#
# sys.stdin = StringIO(test_input1)

size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

primary = []
secondary = []
for idx in range(size):
    primary.append(matrix[idx][idx])
    secondary.append(matrix[idx][size - idx - 1])
print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}" )


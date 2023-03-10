import sys
from io import StringIO
test_input1 = """3
11 2 4
4 5 6
10 8 -12
"""

test_input2 = """3
1 2 3
4 5 6
7 8 9
"""

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

def get_primary_diagonal(matrix):
    the_sum = 0
    n = len(matrix)
    # for r in range(len(n)):
    #     for c in range(n):
    #         if r == c:
    #             the_sum += matrix[r][c]

    # for i in range(n):  # why we know that the indexes are equal
    #     the_sum += matrix[i][i]
    # return the_sum

    return sum(matrix[i][i] for i in range(n))

def get_secondary_diagonal(matrix):
    return sum(matrix[i][n - i - 1] for i in range(n))

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split(" ")]
    )

print(get_primary_diagonal(matrix))
# print(get_secondary_diagonal(matrix))

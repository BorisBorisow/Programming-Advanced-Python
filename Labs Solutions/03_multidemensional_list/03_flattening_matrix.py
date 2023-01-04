n = int(input())

result = []
result_set = set()
for _ in range(n):
    row = [int(x) for x in input().split(", ")]

    result.append(row)

print([v for row in result for v in row])
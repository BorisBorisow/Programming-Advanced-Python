n = input().split()

set_1 = set(int(input()) for x in range(int(n[0])))
set_2 = set(int(input()) for x in range(int(n[1])))
result = set_1.intersection(set_2)

for el in result:
    print(el)

# n, m = [int(x) for x in input().split()]
#
# first = set()
# second = set()
#
# for _ in range(n):
#     first.add(int(input()))
#
# for _ in range(m):
#     second.add(int(input()))
#
# print(first)
# print(second)
# result = first.intersection(second)
# print(*result, sep="\n")
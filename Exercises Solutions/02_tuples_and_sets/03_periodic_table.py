n = int(input())

result = set()

for _ in range(n):
    current_set = set(input().split())
    result = result.union(current_set)  # here we use a union func

# for el in result:
#     print(el)

# [print(el) for el in result]

print(*result, sep='\n')
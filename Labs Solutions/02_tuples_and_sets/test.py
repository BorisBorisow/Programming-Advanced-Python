rows = int(input())

even_numbers_set = set()
odd_numbers_set = set()

for row in range(1, rows + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // row
    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)


if sum(even_numbers_set) == sum(odd_numbers_set):
    result = odd_numbers_set.union(even_numbers_set)
elif sum(even_numbers_set) < sum(odd_numbers_set):
    result = odd_numbers_set.difference(even_numbers_set)
elif sum(even_numbers_set) > sum(odd_numbers_set):
    result = odd_numbers_set.symmetric_difference(even_numbers_set)

print(*result, sep=", ")

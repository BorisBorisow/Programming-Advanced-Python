numbers = input().split("|")

result = []

for idx in range(len(numbers) - 1, -1, - 1):
    current_element = numbers[idx].split()
    result.extend(current_element)
print(*result)
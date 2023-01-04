line = list(map(float, input().split()))

numbers = {}

for num in line:
    if num not in numbers:
        numbers[num] = 0
    numbers[num] += 1

for key, value in numbers.items():
    print(f"{key} - {value} times")
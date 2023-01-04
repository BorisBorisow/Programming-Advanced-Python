from collections import deque

numbers = [int(x) for x in input().split(", ")]
searched_idx = int(input())
# sorted_numbers = deque(sorted((numbers[idx], idx)for idx in range(len(numbers))))
sorted_numbers = deque(sorted([(number, index) for index, number in enumerate(numbers)]))
result = 0

# for nums in sorted_numbers:
# num, idx = nums
while sorted_numbers:
    num, idx = sorted_numbers.popleft()
    result += num
    if idx == searched_idx:
        break
print(result)

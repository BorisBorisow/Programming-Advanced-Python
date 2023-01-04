from collections import deque

def best_list_pureness(numbers, k):
    data = {}
    numbers = deque(numbers)

    for rotation in range(k + 1):
        result = sum([index*value for index, value in enumerate(numbers)])
        data.update({rotation: result})
        numbers.appendleft(numbers.pop())

    max_num_pureness = max(data.values())

    for key, value in data.items():
        if value == max_num_pureness:
            return f"Best pureness {max_num_pureness} after {key} rotations"



test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

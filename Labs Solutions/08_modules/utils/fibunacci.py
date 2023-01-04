def create(n):
    if n == 1:
        return [0]
    if n == 0:
        return []
    result = [0, 1]
    for _ in range(n - 2):
        result.append(result[-1] + result[-2])
    return result


# index of
def locate(target, nums):
    result = -1
    for idx in range(len(target)):
        current_num = target[idx]
        if current_num == target:
            return idx
    return -1

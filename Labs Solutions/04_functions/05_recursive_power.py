def recursive_power(value, power):
    result = 1
    if value == 0:
        return result

    if power == 1:
        return value

    return value * recursive_power(value, power - 1)

print(recursive_power(2, 10))
print(recursive_power(10, 100))
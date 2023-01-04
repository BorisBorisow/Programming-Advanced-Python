def func_executor(*args):
    result = []
    for func_ref, func_nums in args:
        result_func = func_ref(*func_nums)
        result.append(f"{func_ref.__name__} - {result_func}")
    return "\n".join(result)



def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))

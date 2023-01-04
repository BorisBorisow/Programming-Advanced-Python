# ------------------------------60/100 Points--------------------

# def operate(operation, *args):
#     def add(*args):
#         return sum(args)
#     def subract(x, *args):
#         return x - sum(-y for y in args[1:])
#     def devide(x, *args):
#         result = x
#         for value in args[1:]:
#             result /= value
#         return result
#     def multiply(*args):
#         result = 1
#         for value in args:
#             result *= value
#         return result
#
#     if operation == "+":
#         return add(*args)
#     elif operation == "-":
#         return subract(*args)
#     elif operation == "/":
#         return devide(*args)
#     elif operation == "*":
#         return multiply(*args)
#     else:
#         return None
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))


import functools


def operate(opers, *args):
    result = 0
    if opers == '+':
        result = functools.reduce(lambda x, y: x + y, args)
    elif opers == '-':
        result = functools.reduce(lambda x, y: x - y, args)
    elif opers == '*':
        result = functools.reduce(lambda x, y: x * y, args)
    elif opers == '/':
        result = functools.reduce(lambda x, y: x / y, args)

    return result
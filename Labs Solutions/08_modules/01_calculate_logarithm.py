# from math import log
#
# number = int(input())
# base = input()
#
# if base == "natural":
#     print(f"{log(number):.2f}")
# else:
#     print(f"{log(number, int(base)):.2f}")

from math import log, e

number = int(input())
base_input = input()

base = e if base_input == "natural" else int(base_input)
print(f"{log(number, base):.2f}")

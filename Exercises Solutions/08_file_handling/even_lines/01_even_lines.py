import re


def replace_symbols(line):
    return re.sub(r"[-\,\.\!\?]", "@", line)


with open("text.txt", "r") as file:
    lines = file.readlines()
    for row_number in range(len(lines)):  # for row in range(0, len(text), 2):
        if row_number % 2 == 0:  #
            replaced = replace_symbols(lines[row_number]).split()
            print(" ".join(replaced[::-1]))



# def even(file):
#     result = ""
#     symbols = ["-", ",", ".", "!", "?"]
#
#     with open(file, 'r') as f:
#         text = f.readlines()
#
#     for row in range(0, len(text), 2):
#         for symbol in symbols:
#             text[row] = text[row].replace(symbol, '@')
#
#         result += " ".join(text[row].split()[::-1]) + '\n'
#
#     f.close()
#
#     return result

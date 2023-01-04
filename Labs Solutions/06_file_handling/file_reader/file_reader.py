# file = open("numbers.txt", "r")
# result = 0
# for line in file:
#     result += int(line)
# file.close()
# print(result)
#


# -------------------------Second_way-------------------------
with open("numbers.txt", "r") as file:
    result = sum([int(x) for x in file])
    print(result)

# # -------------------------Third_way--------------------------
# print(sum([int(x) for x in open("numbers.txt", "r")]))

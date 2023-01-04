# lines = int(input())
#
# names = []
#
# for i in range(lines):
#     names.add(input())
#
# unique = set(name for name in names)
#
# print(unique)


# ---------------------2---------------------------
lines = int(input())
names = set() # not {}

for i in range(lines):
    names.add(input())

for name in names:
    print(name)

# --------------------3----------------

# n = int(input())
# name_set = {input() for _ in range(n)}
# [print(name) for name in name_set]

# ----------------------4-------------
# Don't do this - 2.06h Mai 2022 Lab
# [print(name) for name in {input() for _ in range(int(input()))}]
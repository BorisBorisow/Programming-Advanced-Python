first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))

rows = int(input())

for _ in range(rows):
    data = input().split()
    command = data[0]
    target_set = data[1]

    if command == "Add":
        if target_set == "First":
            first_set = first_set.union([int(x) for x in data[2:]])
        else:
            second_set = second_set.union([int(x) for x in data[2:]])
    elif command == "Remove":
        if target_set == "First":
            first_set = first_set.difference([int(x) for x in data[2:]])
        else:
            second_set = second_set.difference([int(x) for x in data[2:]])
    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))


print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


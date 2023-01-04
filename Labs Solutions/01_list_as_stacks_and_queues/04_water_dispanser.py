from collections import deque

liters = int(input())
line = deque()
name = input()

while not name == "Start":
    line.append(name)
    name = input()

command = input()

while not command == "End":
    if command.isdigit():
        required_litters = int(command)
        name = line.popleft()
        if liters >= required_litters:
            liters -= required_litters
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    else:
        _, liters_to_fill = command.split()
        liters_to_fill = int(liters_to_fill)
        liters += liters_to_fill
    command = input()

print(f"{liters} liters left")

from collections import deque

elfs = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())

energy_cost = 0
toys = 0
turn = 0

while elfs and materials:
    turn += 1
    current_elf = elfs.popleft()
    current_material = materials.pop()

    if turn % 3 == 0:
        if current_elf >= current_material * 2:
            toys += 2
            energy_cost += current_elf
            if current_elf > 0:
                current_elf += 1
                elfs.append(current_elf)

    elif turn % 5 == 0:
        if current_elf >= current_material:
            toys += 2
            energy_cost += current_elf
            if current_elf > 0:
                current_elf += 1
                elfs.append(current_elf)
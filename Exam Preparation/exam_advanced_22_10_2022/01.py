from collections import deque

coffeine_milligrams = deque(int(x) for x in input().split(", "))
energy_drinks = deque(int(x) for x in input().split(", "))

max_coffeine = 300
sum_coffeine = 0

while coffeine_milligrams and energy_drinks and sum_coffeine != 300:
    current_coffeine = coffeine_milligrams.pop()
    current_drink = energy_drinks.popleft()
    current_sum = current_drink * current_coffeine

    if max_coffeine >= current_coffeine * current_drink:
        if sum_coffeine + (current_coffeine * current_drink) <= 300:
            sum_coffeine += current_coffeine * current_drink
            max_coffeine -= current_coffeine * current_drink
    else:
        if sum_coffeine >= 30:
            sum_coffeine -= 30
            max_coffeine += 30
        energy_drinks.append(current_drink)

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str,energy_drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {sum_coffeine} mg caffeine.")
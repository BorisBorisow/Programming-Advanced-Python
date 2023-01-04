from collections import deque

total_food = int(input())
orders = deque(map(int, input().split()))
print(max(orders))

while orders:
    current_order = orders[0]

    if current_order > total_food:
        break

    total_food -= current_order
    orders.popleft()

if orders:
    print(f"Orders left: {' '.join(map(str,orders))}")
else:
    print("Orders complete")
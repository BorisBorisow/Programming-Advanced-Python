# list of n "0"
ll = []
n = 10

for _ in range(n):
    ll.append(0)

print(ll)


# matric of NxM "0"
n = 7
m = 7

mm = []

for i in range(n):
    ll = []

    for j in range(m):
        ll.append(i * n + j)
    mm.append(ll)

print(mm)


n = int(input())

usernames = set()

for _ in range(n):
    usernames.add(input())

for user in usernames:
    print(user)
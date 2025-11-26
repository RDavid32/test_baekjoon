import sys
input = sys.stdin.readline
t, m = map(int,input().split())
inventory = {i : [] for i in range(1, m+1)}
location = [1 for _ in range(m+1)]

cheating = set()
block = set()

for _ in range(t):
    num, player, action, *target = input().split()
    num, player, target = int(num), int(player), list(map(int, target))
    if action == 'M':
        location[player] = target[0]
    elif action == "F":
        if location[player] != target[0]:
            cheating.add(num)
        inventory[player].append(target[0])
    elif action == "C":
        for i in target:
            if i in inventory[player]:
                inventory[player].remove(i)
            else:
                cheating.add(num)
    else:
        if location[player] != location[target[0]]:
            block.add(player)
            cheating.add(num)

if cheating:
    print(len(cheating))
    print(*sorted(list(cheating)))
else:
    print(0)

if block:
    print(len(block))
    print(*sorted(list(block)))
else:
    print(0)
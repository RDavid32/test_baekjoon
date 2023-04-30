import sys
input = sys.stdin.readline

n, m = map(int,input().split())

truth = set(input().split()[1:])
party = []

for q in range(m):
    party.append(set(input().split()[1:]))

for q in range(m):
    for check in party:
        if check & truth :
            truth = truth.union(check)

result = 0
for q in party:
    if q & truth:
        continue
    result+=1

print(result)
    
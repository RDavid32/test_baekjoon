import sys
input = sys.stdin.readline

n = int(input())
money = [0 for _ in range(1002)]

for _ in range(n):
    d, c = input().split()
    c = int(c)
    if d == "jinju":
        jinju = c
    elif c > 1000:
        money[1001] += 1
    else:
        money[c] += 1

answer = sum(money[jinju+1:])

print(jinju)
print(answer)
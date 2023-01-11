import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for q in range(1, N + 1):
    a = input().rstrip()
    dict[q] = a
    dict[a] = q

for w in range(M):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])
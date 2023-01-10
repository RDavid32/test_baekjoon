import sys
n, m, b = map(int, sys.stdin.readline().split())
mine = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
answer = 1000000000000000000000000000000
for q in range(257):
    max = 0
    min = 0
    for w in range(n):
        for e in range(m):
            if mine[w][e] < q:
                min += (q - mine[w][e])
            else:
                max += (mine[w][e] - q)
    block = max + b
    if block < min:
        continue
    time = 2 * max + min
    if time <= answer:
        answer = time
        height = q
print(answer, height)
import sys
input = sys.stdin.readline
n = int(input())

time = [[0 for _ in range(2)] for _ in range(n)]
for q in range(n):
    s, e = map(int,input().split())
    time[q][0] = s
    time[q][1] = e


time.sort(key = lambda x: (x[1], x[0]))
e = time[0][1]
result = 1
for w in range(1, n):
    if time[w][0] >= e:
        result += 1
        e = time[w][1]

print(result)
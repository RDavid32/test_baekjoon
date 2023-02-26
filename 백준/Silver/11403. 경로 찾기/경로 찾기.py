import sys
input = sys.stdin.readline

n = int(input())
g = [[0 for _ in range(n)] for _ in range(n)]

for q in range(n):
    g[q] = list(map(int,input().split()))

for q in range(n):
    for w in range(n):
        for e in range(n): 
            if g[w][e] == 1 or (g[w][q] == 1 and g[q][e] == 1 ):
                g[w][e] = 1

for row in g:
    for col in row:
        print(col, end = " ")
    print()
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
result = n * m

direction = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}

graph = [list(input().strip()) for _ in range(n)]


parent = [[(x, y) for x in range(m)] for y in range(n)]
visited = [[False] * m for _ in range(n)]


def find(a):
    x, y = a
    if parent[y][x] == a:
        return a
    parent[y][x] = find(parent[y][x])
    return parent[y][x]


def union(a, b):
    global result
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return
    
    parent[rb[1]][rb[0]] = ra
    result -= 1


def dfs(x, y):
    visited[y][x] = True

    dx = x + direction[graph[y][x]][0]
    dy = y + direction[graph[y][x]][1]


    union((x, y), (dx, dy))

    if not visited[dy][dx]:
        dfs(dx, dy)


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(j, i)

print(result)
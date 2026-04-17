import sys

sys.setrecursionlimit(10 ** 8)

def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)

    if rank[r1] > rank[r2]:
        parent[r2] = r1
    elif rank[r1] < rank[r2]:
        parent[r1] = r2
    else:
        parent[r2] = r1
        rank[r1] += 1


def find(v):
    if v == parent[v]:
        return v
    parent[v] = find(parent[v])
    return parent[v]


n, m = map(int,sys.stdin.readline().strip().split())
parent = [i for i in range(n)]
rank = [0 for _ in range(n)]


def solve():
    for i in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        if find(a) == find(b):
            print(i + 1) 
            return
        union(a, b)
    print(0)
    return

solve()
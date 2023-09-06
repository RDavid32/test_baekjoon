import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

parent = [0 for _ in range(n+1)]
for q in range(1, n+1):
    parent[q] = q
    
    
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
result = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    edges.append((c,a,b))

edges.sort()

for q in range(m):
    cost, a, b = edges[q]
    
    if (find_parent(parent, a) != find_parent(parent, b)):
        union_parent(parent, a, b)
        result += cost

print(result)
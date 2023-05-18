from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for q in range(n+1)]

for q in range(n-1):
    a, b = map(int,input().split())
    tree[b].append(a)
    tree[a].append(b)
queue = deque()

queue.append(1)
result = [0] *(n+1)

while queue:
    node = queue.popleft()
    for q in tree[node]:
        if result[q] == 0:
            result[q] = node
            queue.append(q)


for q in result[2:]:
    print(q)
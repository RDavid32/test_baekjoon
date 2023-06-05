from collections import deque
import sys
input = sys.stdin.readline 
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(go, result):
    queue = deque([go])

    while queue:
        x,y = queue.popleft()
        for q in range(4):
            x1 = x + dx[q]
            y1 = y + dy[q]
            if 0 <= x1 < n and  0<= y1 < m and arr[x1][y1] and not result[x1][y1]:
                queue.append([x1,y1])
                result[x1][y1] += result[x][y] + 1
        
n,m = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
for x,q in enumerate(arr):
    for y,w in enumerate(q):
        if w == 2:
            start = [x,y]
            break
result = [[0 for _ in range(m)] for q in range(n)]
bfs(start,result)


for x,q in enumerate(arr):
    for y,w in enumerate(q):
        if w and not result[x][y]:
            result[x][y] = -1
x,y = start
result[x][y] = 0
for q in result:
    print(*q)
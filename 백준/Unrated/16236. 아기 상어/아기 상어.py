import sys
from collections import deque
input=sys.stdin.readline

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

def bfs(a, b):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[a,b]])
    check = []

    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for q in range(4):
            x1, y1 =x + dx[q] , y + dy[q]

            if 0 <= x1 and x1 < N and 0 <= y1 and y1 < N and visited[x1][y1] == 0:

                if space[a][b] > space[x1][y1] and space[x1][y1] != 0:
                    visited[x1][y1] =  visited[x][y] + 1
                    check.append((visited[x1][y1] - 1, x1, y1))

                elif space[a][b] == space[x1][y1]:
                    visited[x1][y1] =  visited[x][y] + 1
                    queue.append([x1,y1])

                elif space[x1][y1] == 0:
                    visited[x1][y1] =  visited[x][y] +1
                    queue.append([x1,y1])
                    

    return sorted(check, key = lambda x: (x[0], x[1], x[2]))

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

location = []
for q in range(N):
    for w in range(N):
        if space[q][w] == 9:
            location.append(q)
            location.append(w)

cnt = 0
q, w = location
size = [2, 0]

while True:
    space[q][w] = size[0]
    queue1 = deque(bfs(q,w))
    
    if not queue1:
        break

    step, x, y = queue1.popleft()
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[q][w] = 0
    q, w = x, y

print(cnt)
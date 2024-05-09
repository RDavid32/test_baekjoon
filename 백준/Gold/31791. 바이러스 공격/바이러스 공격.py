from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int,input().split())
TG, TB, X, B = map(int,input().split())
grid = []
for i in range(N):
    grid.append(list(input()))

visited = [[False] * M for _ in range(N)]
virus = [[False] * M for _ in range(N)]
que = deque()
bque = deque()

for i in range(N):
    for j in range(M):
        if grid[i][j] == '*':
            que.append((i, j, 0))
            visited[i][j] = True

def in_range(y, x):
    return 0 <= y < N and 0 <= x < M

while que or bque:
    if not que:
        y, x, t = bque.popleft()
    elif not bque:
        y, x, t = que.popleft()
    else:
        if que[0][2] < bque[0][2]:
            y, x, t = que.popleft()
        else:
            y, x, t = bque.popleft()

    if t > TG:
        break

    virus[y][x] = True
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = y + dy, x + dx
        if not in_range(ny, nx) or visited[ny][nx]:
            continue

        visited[ny][nx] = True
        if grid[ny][nx] == '#':
            bque.append((ny, nx, t + TB + 1))
        else:
            que.append((ny, nx, t + 1))

answer = []
for i in range(N):
    for j in range(M):
        if not virus[i][j]:
            answer.append((i + 1, j + 1))

if not answer:
    print(-1)
    
else:
    for y, x in answer:
        print(y, x)


from collections import deque

n, m = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
size = 0

def bfs(x, y):
    global visited
    que = deque()
    que.append((x, y))
    visited[y][x] = True
    area = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((nx, ny))
                    area += 1

    return area


board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            size = max(size, bfs(j, i))
            count += 1

print(count)
print(size)
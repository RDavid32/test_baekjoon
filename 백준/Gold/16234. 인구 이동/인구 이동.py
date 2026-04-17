from collections import deque

n, l, r = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

answer = 0
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(sx, sy):
    que = deque([(sx, sy)])
    visited[sy][sx] = True
    
    union = [(sx, sy)]
    total = arr[sy][sx]
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if l <= abs(arr[y][x] - arr[ny][nx]) <= r:
                    visited[ny][nx] = True
                    que.append((nx, ny))
                    union.append((nx, ny))
                    total += arr[ny][nx]
    
    if len(union) == 1:
        return 0
    
    new_value = total // len(union)
    
    for x, y in union:
        arr[y][x] = new_value
    
    return 1


while True:
    visited = [[False]*n for _ in range(n)]
    move = 0
    
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                move += bfs(x, y)
    
    if move == 0:
        break
    
    answer += 1

print(answer)

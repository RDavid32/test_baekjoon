from collections import deque

H, W = map(int, input().split())
dir = [(-1,0), (1,0), (0,-1), (0,1), (1,-1), (1,1), (-1,-1), (-1,1)]
board = [list(input()) for _ in range(H)]
visited = [[0 for _ in range(W)] for _ in range(H)]
dq = deque()
for i in range(H):
    for j in range(W):
        if board[i][j] == '.':
            board[i][j] = 0 
            dq.append((i, j))
        else:
            board[i][j] = int(board[i][j])    
answer = 0

while len(dq):    
    y, x = dq.popleft()
    for k in range(len(dir)):
        ny = y + dir[k][0]
        nx = x + dir[k][1]
        if 0 > ny or ny >= H or 0 > nx or nx >= W:
            continue

        if board[ny][nx] != 0:
            board[ny][nx] -= 1
            if board[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1 
                answer = max(answer, visited[ny][nx])
                dq.append((ny, nx))

print(answer)
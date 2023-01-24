import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            x1 = x + dx[q]
            y1 = y + dy[q]
            if 0<= x1 < m and 0<= y1 <n and field[x1][y1] == 0:
                field[x1][y1] = field[x][y]+1
                queue.append([x1,y1]) 

    return


if __name__ == "__main__":
    queue = deque([])

    n, m = map(int,input().split())
    field = [0 for _ in range(m)]

    for q in range(m):
        field[q] = list(map(int,input().split()))

    for a in range(n):
        for b in range(m):
            if field[b][a] == 1:
                queue.append([b,a])
    bfs()

    for a in range(n):
        for b in range(m):
            if field[b][a] == 0:
                print(-1)
                exit(0)
 
    result = max(map(max, field))
    print(result-1)
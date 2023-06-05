from collections import deque
import sys
input = sys.stdin.readline 
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start, check):
    result =0
    queue = deque([start])
    while queue:
        x,y = queue.popleft()
        for q in range(4):
            x1 = x + dx[q]
            y1 = y + dy[q]
            if 0 <= x1 < n and 0<= y1 < m and arr[x1][y1] != 'X' and not check[x1][y1]:
                if arr[x1][y1] == 'P': 
                    result += 1
                check[x1][y1] =  True
                queue.append([x1,y1])

    return result

n, m = map(int,input().strip().split())
arr = [list(input()) for _ in range(n)]

check = [[False for _ in range(m)] for _ in range(n)]
for x, q in enumerate(arr):
    for y,w in enumerate(q):
        if w == 'I':
            check[x][y] == True
            start = [x,y]
            break

if result := bfs(start,check):
    print(result)
else:
    print('TT')
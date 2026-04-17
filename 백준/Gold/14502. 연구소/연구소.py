from collections import deque
n, m = map(int,input().split())

dx = [-1, 0 ,1 ,0]
dy = [0, -1, 0, 1]
arr  = [list(map(int,input().split()))for _ in range(n)]
answer = 0

queue = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            queue.append([i,j])

count_zero = sum(i.count(0) for i in arr)

def bfs(lab, que):
    
    count = 0

    while que:
        
        y, x = que.popleft()
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < m and 0 <= y1 < n and not lab[y1][x1]:
                lab[y1][x1] = 2
                count += 1
                que.append([y1, x1])

    return count_zero - count

for i in range(n * m):
    ix, iy = i % m, i // m
    if arr[iy][ix]:
        continue
    arr[iy][ix] = 1
    for j in range(i, n * m): 
        jx, jy = j % m, j // m
        if arr[jy][jx]:
            continue
        arr[jy][jx] = 1
        for k in range(j, n * m):
            kx, ky = k % m, k // m
            if arr[ky][kx]:
                continue
            arr[ky][kx] = 1

            lab = [row[:] for row in arr]

            answer = max(answer, bfs(lab, queue.copy()))

            arr[ky][kx] = 0
        arr[jy][jx] = 0
    arr[iy][ix] = 0

print(answer - 3)
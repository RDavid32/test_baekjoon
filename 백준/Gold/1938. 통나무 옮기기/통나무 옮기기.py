from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(2)] #0이 가로 1이 세로

arr = [list(input().strip()) for _ in range(n)]

def find_start():
    global start
    for x in range(n):
        for y in range(n):
            if arr[y][x] == "B":
                if x+1 < n and arr[y][x+1] == "B":
                    start = [0, x+1, y, 0] # 0이 가로
                else:
                    start = [1, x, y+1, 0] # 1이 세로
                return
                
def find_end():
    global end   
    for x in range(n):
        for y in range(n):
            if arr[y][x] == "E":
                if x+1 < n and arr[y][x+1] == "E":
                    end = [0, x+1, y, 0]
                else:
                    end = [1, x, y+1, 0]
                return

find_start()
find_end()

que = deque([])
que.append(start)

while que:
    d, x, y, count = que.popleft()

    if [d, x, y] == end[:3]:
        print(count)
        exit()

    count += 1
    if d == 0:
        for i in range(-1, 2, 2):
            dx = x + i
            if 0 <= dx + i < n and arr[y][dx+i] != '1':
                if not visited[d][y][dx]:
                    visited[d][y][dx] = count
                    que.append([d, dx, y, count])
        
        check = 0
        for i in range(-1, 2, 2):
            dy = y + i
            if 0 <= dy < n:
                if all(j != '1' for j in [arr[dy][x-1], arr[dy][x], arr[dy][x+1]]):
                    if not visited[d][dy][x]:
                        visited[d][dy][x] = count
                        que.append([d, x, dy, count])
                    check += 1
                    
        if check == 2:
            if not visited[1][y][x]:   
                visited[1][y][x] = count
                que.append([1, x, y, count])
                
                
    else:
        for i in range(-1, 2, 2):
            dy = y + i
            if 0 <= dy + i < n and arr[dy+i][x] != '1':
                if not visited[d][dy][x]:
                    visited[d][dy][x] = count
                    que.append([d, x, dy, count])
        
        check = 0
        for i in range(-1, 2, 2):
            dx = x + i
            if 0 <= dx < n:
                if all(j != '1' for j in [arr[y-1][dx], arr[y][dx], arr[y+1][dx]]):
                    if not visited[d][y][dx]:
                        visited[d][y][dx] = count
                        que.append([d, dx, y, count])
                    check += 1
        
        if check == 2:
            if not visited[0][y][x]:
                visited[0][y][x] = count
                que.append([0, x, y, count])
        
print(0)
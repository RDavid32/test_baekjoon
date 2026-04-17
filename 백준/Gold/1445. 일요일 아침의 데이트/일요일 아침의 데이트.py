import heapq
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int,input().split())

road = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
q = []

for i in range(n):
    for j in range(m):
        if road[i][j] == "S":
            start_x, start_y = j, i
        elif road[i][j] == "F":
            flower_x, flower_y = j, i
        elif road[i][j] == "g":
            for x, y in zip(dx, dy):
                next_x = j + x
                next_y = i + y
                if 0 <= next_x < m and 0 <= next_y < n and road[next_y][next_x] == ".":
                    road[next_y][next_x] = "n"

count = 0
heapq.heappush(q,(0,0,start_x,start_y)) # 지나가는거, 옆에 가는거, 좌표
visited[start_y][start_x] = True

while q:
    over, side, current_x, current_y = heapq.heappop(q)
    
    for x, y in zip(dx, dy):
        next_x = x + current_x
        next_y = y + current_y
        if 0 <= next_x < m and 0 <= next_y < n and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            if road[next_y][next_x] == ".":
                heapq.heappush(q, (over, side, next_x, next_y))
            elif road[next_y][next_x] == "g":
                heapq.heappush(q, (over+1, side, next_x, next_y))
            elif road[next_y][next_x] == "n":
                heapq.heappush(q, (over, side+1, next_x, next_y))
            else:
                print(over, side)

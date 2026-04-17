n, m = map(int,input().split())
di = {"N": -1, "E": 0, "W": 0, "S": 1}
dj = {"N": 0, "E": 1, "W": -1, "S": 0}
result = 0

road = [list(input()) for _ in range(n)]
parent = [[j*m+i for i in range(m)] for j in range(n)]
visited = [[False for _ in range(m)]for _ in range(n)]

for y in range(n):
    for x in range(m):
        if visited[y][x]:
            continue
        
        path = set()
        
        dy, dx = y, x
        while True:
            if visited[dy][dx]:
                if (dy, dx) in path:
                    result += 1
                break
                
            visited[dy][dx] = True
            path.add((dy, dx))
            
            direction = road[dy][dx] 
            dy += di[direction]
            dx += dj[direction]

print(result)
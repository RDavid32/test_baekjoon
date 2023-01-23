from collections import deque

x1 = [1,-1,0,0]
y1 = [0,0,1,-1]

def bfs(a,b,field):
    queue = deque()
    queue.append((a,b))
    field[a][b] = 0

    while queue:
        x,y = queue.popleft()
        for e in range(4):
            check_x = x + x1[e]
            check_y = y + y1[e]
            if 0 <= check_x <n and 0<= check_y < m:
                if field[check_x][check_y] == 1:
                    field[check_x][check_y] = 0
                    queue.append((check_x,check_y))
    return 0
             
if __name__== "__main__":
    t = int(input())
    for q in range(t):
        result=0
        n, m, k = map(int,input().split())
        field = [[0 for _ in range(m)]for _ in range(n)]
        for w in range(k):
            x, y = map(int,input().split())
            field[x][y] = 1
        
        for a in range(n):
            for b in range(m):
                if field[a][b] == 1:
                    bfs(a,b,field)
                    result+=1
        print(result)
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():


    while queue:
        x,y,z=queue.popleft() 

        for q in range(6):
            x1 = x+dx[q]
            y1 = y+dy[q]
            z1 = z+dz[q]
            if 0<=x1 < h and 0<=y1<n and 0<=z1<m and table[x1][y1][z1]==0 :
                table[x1][y1][z1] = table[x][y][z]+1
                queue.append([x1,y1,z1])

        #queue += graph[n] - set(visited)
    return 


m,n,h = map(int,input().split())

table = []
queue=deque([])
for q in range(h):
    note=[]
    for w in range(n):
        note.append(list(map(int,input().split())))
        for e in range(m):
            if note[w][e] == 1:
                queue.append([q,w,e])
    table.append(note)

bfs()

result=0
for a in range(h):
        for b in range(n):
            for c in range(m):
                if table[a][b][c] == 0:
                    print(-1)
                    exit(0)
                result = max(result,table[a][b][c])


print(result-1)
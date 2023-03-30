from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(color,x,y,check):
    while queue:
        x,y = queue.popleft()
        for q in range(4):
            x1 = x + dx[q]
            y1 = y + dy[q]
            if 0<=x1<n and 0<=y1<n and check == color[x1][y1]:
                queue.append([x1,y1])
                color[x1][y1] = count

    return color
n = int(input())
RGB = []
RRB = []
for q in range(n):
    table = list(input())
    del table[n]
    RGB.append(table[:])
    RRB.append(table)
queue = deque()

count = 0
for q in range(n):
    for w in range(n):
        if type(RGB[q][w]) == str:
            count+=1
            check = RGB[q][w]
            queue.append([q,w])
            RGB = bfs(RGB,q,w,check)
result1 = count        
count = 0
for a in range(n):
    for b in range(n):
        if RRB[a][b] == 'G':
            RRB[a][b] = 'R'

for q in range(n):
    for w in range(n):
        if type(RRB[q][w]) == str:
            count+=1
            check = RRB[q][w]
            queue.append([q,w])
            RRB = bfs(RRB,q,w,check)


result2 = count
print(result1, result2)
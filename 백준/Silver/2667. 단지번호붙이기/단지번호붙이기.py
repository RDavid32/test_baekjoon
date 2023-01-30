from collections import deque
import sys

input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]


n = int(input())

house = [0 for q in range(n)]
for q in range(n):
  house[q] = list(input())

def bfs(house,root):
  queue = deque([root])
  count=0
  while queue:
    x,y = queue.popleft()
    if house[x][y] == '1':
      count+=1
      house[x][y] = '0'
      for q in range(4):
        if 0<=x+dx[q]<n and 0<=y+dy[q]<n:
          queue.append([x+dx[q],y+dy[q]])
  return(count)

result = []
for q in range(n):
  for w in range(n):
    if house[q][w] == '1':
      result.append(bfs(house,[q,w]))
print(len(result))
result.sort()
for e in result:
  print(e)
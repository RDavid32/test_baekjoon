from collections import deque
import sys
input = sys.stdin.readline


x = int(input())


queue = deque([(0, x)])
visited = {}

while True:
    cnt, x = queue.popleft()
    if x == 1:
        print(cnt)
        break
    
    if x % 3 == 0 and x // 3 not in visited:
        visited[x // 3] = cnt + 1
        queue.append((cnt + 1, x // 3))
        
    if x % 2 == 0 and x // 2 not in visited:
        visited[x // 2] = cnt + 1
        queue.append((cnt + 1, x // 2))
        
    if x - 1 not in visited:
        visited[x - 1] = cnt + 1
        queue.append((cnt + 1, x - 1))
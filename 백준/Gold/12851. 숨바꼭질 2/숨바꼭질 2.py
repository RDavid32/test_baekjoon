from collections import deque
import sys
input = sys.stdin.readline
INF = 100001
n, k = map(int,input().split())

visited = [-1 for _ in range(INF)]
queue = deque([n])
visited[n]= 0
result = 0
while queue:
    num = queue.popleft()
    
    if num == k:
        result += 1

    for i in [num-1, num+1, 2*num]:
        if 0 <= i < INF and (visited[i] == visited[num] + 1 or visited[i] == -1):
            queue.append(i)
            visited[i] = visited[num] + 1

print(visited[k])
print(result)
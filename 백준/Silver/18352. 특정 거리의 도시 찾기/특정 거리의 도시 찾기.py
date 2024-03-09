from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        check = queue.popleft()
        for q in graph[check]:
            if not visited[q]:
                visited[q] = True
                queue.append(q)
                distance[q] = distance[check] + 1
                if distance[q] == K:
                    answer.append(q)

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for q in answer:
            print(q, end='\n')

bfs(X)
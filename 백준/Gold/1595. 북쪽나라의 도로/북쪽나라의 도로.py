from collections import deque

def bfs(start, visit):

    que = deque([start])
    visit[start] = 0
    while que:
        x = que.popleft()
        for q, w in graph[x]:
            if visit[q] == -1:
                que.append(q)
                visit[q] = visit[x] + w
        



graph = [[] for _ in range(10001)]
while True:
    try:
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    except:
        break
result = 0
visit = [-1 for _ in range(10001)]
bfs(1,visit)
new_start = visit.index(max(visit))
visit = [-1 for _ in range(10001)]

bfs(new_start,visit)
print(max(visit))

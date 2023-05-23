import heapq
import sys
input = sys.stdin.readline
INF = 1e8
n,m = map(int,input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for q in range(m):
    u, v , w = map(int,input().split())
    graph[u].append((v,w))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            check = dist + i[1]

            if check < distance[i[0]]:
                distance[i[0]] = check
                heapq.heappush(q, (check, i[0]))
    
dijkstra(start)
for q in distance[1:]:
    if q == INF:
        print("INF")
    else:
        print(q)
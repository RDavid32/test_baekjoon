import heapq
import sys
input = sys.stdin.readline
INF = 1e8
n  = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    
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
start,end = map(int,input().split())
dijkstra(start)
print(distance[end])
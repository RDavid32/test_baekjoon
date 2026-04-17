import heapq
n = int(input())
m = int(input())
INF = 1e8
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
road = [[i] for i in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

start, end = map(int,input().split())
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) 

    if distance[now] < dist: 
      continue               

    for i in graph[now]:     

      if dist + i[1] < distance[i[0]]: 
        distance[i[0]] = dist+i[1]
        road[i[0]] = road[now] + [i[0]]
        heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(start)
print(distance[end])
print(len(road[end]))
print(*road[end])
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

def dijkstra(start):
    q=[]
    distance = [INF] * (n+1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q:
        dist ,idx= heapq.heappop(q)
        
        if distance[idx] < dist:
            continue
        
        for node_idx , node_dist in graph[idx]:
            total_dist = node_dist + dist
            
            if distance[node_idx] > total_dist:
                distance[node_idx] = total_dist
                heapq.heappush(q,(total_dist,node_idx))
    return distance
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

result = 0
for q in range(1,n+1):
    start = dijkstra(q)
    end = dijkstra(x)
    result = max(result, start[x] +  end[q])
print(result)
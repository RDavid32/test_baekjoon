import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
depth = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

n_dpeth =1
def dfs(v):
    global n_dpeth
    depth[v] = n_dpeth
    n_dpeth +=1
    for nx in sorted(graph[v],reverse =True ):
        if visited[nx] == -1:
            visited[nx] = visited[v]+1
            dfs(nx)
visited[r] = 0
dfs(r)
result = 0 
for i in range(1, n + 1):
    if visited[i] != -1:
        result += (depth[i]* visited[i]) 
print(result)
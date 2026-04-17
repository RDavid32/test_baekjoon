import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            dp[start][0] += dp[i][1]
            dp[start][1] += min(dp[i][0], dp[i][1])


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
dp = [[0, 1] for _ in range(n + 1)]

dfs(1)
print(min(dp[1][0], dp[1][1]))
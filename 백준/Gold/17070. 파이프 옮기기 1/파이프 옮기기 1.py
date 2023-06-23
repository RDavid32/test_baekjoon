import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]

for q in range(n):
    graph[q] = list(map(int, input().split()))

dp[0][0][1] = 1  

for q in range(2, n):
    if graph[0][q] == 0:
        dp[0][0][q] = dp[0][0][q - 1]

for w in range(1, n):
    for e in range(1, n):
        if graph[w][e] == 0 and graph[w][e - 1] == 0 and graph[w - 1][e] == 0:
            dp[2][w][e] = dp[0][w - 1][e - 1] + dp[1][w - 1][e - 1] + dp[2][w - 1][e - 1]

        if graph[w][e] == 0:
            dp[0][w][e] = dp[0][w][e - 1] + dp[2][w][e - 1]
            dp[1][w][e] = dp[1][w - 1][e] + dp[2][w - 1][e]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))
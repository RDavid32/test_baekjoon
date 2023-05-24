import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0, 0]]

for _ in range(n):
    bag.append(list(map(int, input().split())))
    
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = bag [i][0]
        value = bag [i][1]
        
        dp[i][j] = max(bag[i][1] + dp[i - 1][j - bag[i][0]], dp[i - 1][j]) if j - bag[i][0] >= 0 else dp[i - 1][j]

print(dp[n][k])

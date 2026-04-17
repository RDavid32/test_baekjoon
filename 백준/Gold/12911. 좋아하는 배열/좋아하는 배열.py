n,k = map(int,input().split())
mod = 1000000007
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
sum = [0 for _ in range(n+1)]
for i in range(1,k+1): dp[1][i] = 1
sum[1] = k

for i in range(2, n+1):
    for j in range(1, k+1):
        dp[i][j] += sum[i-1]
        for l in range(j*2,k+1, j):
            dp[i][j] -= dp[i-1][l]
        sum[i] += dp[i][j]
        sum[i] %= mod

print(sum[n]%mod)
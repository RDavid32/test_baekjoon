n = int(input())

dp = [0] * (n+1)
dp[0] = 1

two = [2 ** q for q in range(21)]

for q in two:
    if q <= n:
        for w in range(q, n+1):
            dp[w] += (dp[w - q]) % 1000000000

print(dp[n] % 1000000000)
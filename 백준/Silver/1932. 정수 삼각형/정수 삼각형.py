import sys
input = sys.stdin.readline
n = int(input())
dp = []

for q in range(n):
    dp.append(list(map(int, input().split())))

for q in range(1, n):
    for w in range(q+1):
        if w == 0:
            dp[q][w] = dp[q][w] + dp[q - 1][w]
        elif q == w:
            dp[q][w] = dp[q][w] + dp[q - 1][w - 1]
        else:
            dp[q][w] = max(dp[q - 1][w - 1], dp[q - 1][w]) + dp[q][w]
    
print(max(dp[n - 1]))
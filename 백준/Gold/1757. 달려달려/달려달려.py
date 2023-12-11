from copy import deepcopy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
run = [int(input()) for _ in range(n)]


dp = [[0] * 2 for _ in range(m + 2)]
dp[1][1] = run[0]

for q in range(1, n):
    next = [[0] * 2 for _ in range(m + 2)]
    next[0][0] = max(dp[0][0], dp[1][1], dp[1][0])
    next[1][1] = dp[0][0] + run[q]
    
    for w in range(1, m):
        next[w][0] = max(dp[w][0], dp[w + 1][1], dp[w + 1][0])
        next[w + 1][1] = dp[w][1] + run[q]
    
    dp = deepcopy(next)

print(dp[0][0])
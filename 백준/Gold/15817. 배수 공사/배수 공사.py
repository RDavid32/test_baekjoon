import sys
input = sys.stdin.readline

n, x = map(int, input().split())

dp = [0 for _ in range(x + 1)]
dp[0] = 1

for _ in range(n):
    l, c = map(int, input().split())
    for i in range(x, -1, -1):
        if dp[i] == 0:
            continue
        
        for j in range(1, c + 1):
            if i + l * j > x:
                break
            
            dp[i + l* j] += dp[i]

print(dp[x])
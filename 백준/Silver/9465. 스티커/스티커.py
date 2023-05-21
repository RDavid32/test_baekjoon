import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]
    if l>1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for q in range(2,l):
        dp[0][q] += max(dp[1][q-1], dp[1][q-2])
        dp[1][q] += max(dp[0][q-1], dp[0][q-2])
    print(max(dp[0][l - 1], dp[1][l - 1]))
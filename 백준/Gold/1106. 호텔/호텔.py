import sys
input = sys.stdin.readline
INF = 1e7
c,n = map(int,input().split())
cost_arr = [list(map(int,input().split())) for _ in range(n)]
dp = [INF for _ in range(c+100)]
dp[0]=0
 
for cost, num_people in cost_arr:
    for i in range(num_people, c+100):
        dp[i] = min(dp[i - num_people]+cost, dp[i])
 
print(min(dp[c:]))
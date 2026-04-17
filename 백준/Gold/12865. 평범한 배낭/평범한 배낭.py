import sys
input = sys.stdin.readline
n, m = map(int,input().split())

bag = [[0,0]]
dp = [0 for _ in range(m + 1)]
for i in range(n):
    v, w = map(int,input().split())

    bag.append([v,w])

for i in range(1, n + 1):
    for j in range(m, 0, -1):
        dp[j] = max(bag[i][1] + dp[j - bag[i][0]], dp[j]) if j - bag[i][0] >= 0 else dp[j]

print(dp[m])
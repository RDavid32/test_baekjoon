import sys
n = int(sys.stdin.readline())
dp = [[1,0],[0,1]] 
for q in range(1, 41):
    dp.append([dp[q][0]+dp[q-1][0],dp[q][1]+dp[q-1][1]])
for q in range(n):
    a = int(sys.stdin.readline())
    print(dp[a][0],dp[a][1])
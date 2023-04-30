import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
dp[0][0] = num[0]
if n > 1 :
    result = -1e9
    for q in range(1,n):
        dp[0][q] = max(dp[0][q-1] + num[q], num[q])
        dp[1][q] = max(dp[0][q-1], dp[1][q-1] + num[q])
        result = max(result, dp[0][q], dp[1][q])
        
        
    print(result)
else:
    print(dp[0][0])
import sys
input = sys.stdin.readline

n ,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0] = arr[0][:]

for i in range(1 ,m):
  dp[0][i] += dp[0][i-1]

for i in range(1, n):
  tmpl=[0 for _ in range(m)]
  tmpr=[0 for _ in range(m)]
  
  for j in range(m):
    if j == 0: 
      tmpl[j] = arr[i][j]+ dp[i-1][j] 
      tmpr[m-1-j] = arr[i][m-1-j]+ dp[i-1][m-1-j]
      continue

    tmpl[j] = arr[i][j] + max(dp[i-1][j], tmpl[j-1])
    tmpr[m-1-j]= arr[i][m-1-j] + max(dp[i-1][m-1-j],tmpr[m-j])
  

  dp[i]= [max(tmpl[i], tmpr[i]) for i in range(m)][:]

print(dp[n-1][m-1])
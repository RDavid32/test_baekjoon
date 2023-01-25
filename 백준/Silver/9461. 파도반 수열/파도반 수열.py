import sys
input = sys.stdin.readline

t = int(input())
dp = [0 for _ in range(100)]
dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2

for w in range(5,100):
    dp[w] = dp[w-5] + dp[w-1]

for q in range(t):
    
    print(dp[int(input())-1])
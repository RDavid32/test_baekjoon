import sys
input = sys.stdin.readline

arr = [1, 10, 25]

t = int(input())

dp = [10 ** 15 for _ in range(100)]
dp[0] = 0
for i in arr:
    for j in range(i, 100):
        dp[j] = min(dp[j], dp[j - i] + 1)
    
for _ in range(t):
    x = int(input())
    answer = 0

    while x:
        answer += dp[x%100]
        x //= 100

    print(answer)
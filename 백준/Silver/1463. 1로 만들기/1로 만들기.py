n = int(input())
dp = [0] * (n + 1)	

for q in range(2, n + 1):

    dp[q] = dp[q - 1] + 1
    if q % 3 == 0:
        dp[q] = min(dp[q], dp[q // 3] + 1)	
    if q % 2 == 0:
        dp[q] = min(dp[q], dp[q // 2] + 1)
print(dp[n])
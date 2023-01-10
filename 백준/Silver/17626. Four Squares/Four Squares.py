N = int(input())
dp = [0,1]

for q in range(2, N+1):
    num = 1e9
    w = 1
    while (w**2) <= q:
        num = min(num, dp[q - (w**2)])
        w += 1

    dp.append(num + 1)
print(dp[N])
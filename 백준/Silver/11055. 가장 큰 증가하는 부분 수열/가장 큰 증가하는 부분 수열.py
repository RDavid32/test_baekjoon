n = int(input())
arr = list(map(int,input().split()))

dp = arr[:]

for q in range(1,n):
    for w in range(q):
        if arr[q] > arr[w]:
            dp[q] = max(dp[q], dp[w] + arr[q])

print(max(dp))
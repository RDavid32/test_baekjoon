n = int(input())
arr = list(map(int,input().split()))
dp = [1 for q in range(n)]

for q in range(1, n):
    for w in range(q):
        if arr[q] > arr[w]:
            dp[q] = max(dp[q], dp[w]+1)
print(max(dp))
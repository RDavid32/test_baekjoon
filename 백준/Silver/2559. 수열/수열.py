import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dp = sum(arr[:k])
result = [dp]

for q in range(0, len(arr)-k):
    dp = dp - arr[q] + arr[q+k]
    result.append(dp)

print(max(result))
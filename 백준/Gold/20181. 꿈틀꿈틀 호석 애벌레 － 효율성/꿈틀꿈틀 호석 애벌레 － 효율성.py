import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 0
dp = [0 for _ in range(n)]


tmp = 0 #현재 만족도
check = 0 #지금까지의 합

while True:
    if tmp >= k:
        check = 0 if left == 0 else max(check, dp[left-1])
        dp[right - 1] = max(dp[right - 1], check + tmp - k)
        tmp -= arr[left]
        left += 1
    elif right == n: break
    else:
        tmp += arr[right]
        right += 1
print(max(dp))
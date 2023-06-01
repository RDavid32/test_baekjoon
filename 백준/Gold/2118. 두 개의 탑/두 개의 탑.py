import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n
dp[0] = arr[0]
for q in range(1,n):
    dp[q] += arr[q] + dp[q-1]
result = 0
left = 0
right = 1

while right != n:
    left_num = dp[right] - dp[left]
    right_num = dp[-1] - dp[right] + dp[left]

    if left_num > right_num:
        result = max(result,right_num)
        left+=1
    elif left_num < right_num:
        result = max(left_num,result)
        right += 1
        
    else:
        result = left_num
        break
print(result)
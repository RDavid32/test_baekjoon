import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0 
check = 0 
result = len(arr) + 1

while True:
    if check >= s:
        result = min(result, right - left)
        check -= arr[left]
        left += 1
        
    elif right == n:
        break

    else:
        check += arr[right]
        right += 1

if result == len(arr) +1:
    print(0)
    
else:
    print(result)
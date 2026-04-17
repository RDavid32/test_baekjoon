import math
import sys
input = sys.stdin.readline

n = int(input())

arr = [True]*(n+1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        for j in range(i*2, n+1, i):
            arr[j] = False

arr = [i for i in range(2, n+1) if arr[i]] + [0]

i = 0
j = 0
check = arr[i]
count = 0

while j < len(arr)-1:

    if check == n:
        count += 1
        check -= arr[i]
        i += 1
        j += 1
        check += arr[j]

    elif check < n:
        j += 1
        check += arr[j]

    else:
        check -= arr[i]
        i += 1
        
print(count)
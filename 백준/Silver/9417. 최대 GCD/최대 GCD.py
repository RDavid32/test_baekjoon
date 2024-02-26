import math
import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    result = 1
    arr = list(map(int,input().split()))
    for q in range(len(arr)):
        for w in arr[q+1:]:

            result = max(result,math.gcd(arr[q],w))
    print(result)
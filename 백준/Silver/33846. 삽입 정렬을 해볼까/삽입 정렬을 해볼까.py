import sys
n, t = map(int,input().split())
arr = list(map(int,input().split()))
check = sorted(arr[:t])
print(*check, *arr[t:])
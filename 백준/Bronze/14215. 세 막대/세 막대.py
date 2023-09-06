import sys
input = sys.stdin.readline
arr = list(map(int,input().split()))
arr.sort()

print(arr[0]+ arr[1] + (arr[2] if arr[1] + arr[0] > arr[2] else arr[0] + arr[1] - 1))
import sys
input = sys.stdin.readline 
def round2(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input())
if n:
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    check = round2(n * 0.15)
    print(round2(sum(arr[check:-check] if check else arr) / (n - 2 * check)))
else:
    print(0)
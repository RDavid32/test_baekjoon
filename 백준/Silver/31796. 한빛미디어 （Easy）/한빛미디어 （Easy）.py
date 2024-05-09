n = int(input())
arr = sorted(list(map(int,input().split())))
result = 1
now = arr[0]
for q in range(1,n):
    if arr[q] >= 2*now:
        now = arr[q]
        result += 1
print(result)
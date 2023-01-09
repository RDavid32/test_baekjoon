n, m = map(int, input().split())
wood = list(map(int, input().split()))
start, end = 1, max(wood) 
while start <= end: 
    mid = (start+end) // 2
    count = 0 
    for i in wood:
        if i > mid:
            count += i - mid
    if count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
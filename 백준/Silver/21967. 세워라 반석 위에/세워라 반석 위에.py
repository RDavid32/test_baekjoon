from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
A = defaultdict(int)
inf = 2e9
ans = -inf
A[arr[0]] += 1
start_point, end_point = 0, 0

while start_point < n and end_point < n:
    minn = min(i for i in range(1, 11) if A[i] != 0)
    maxx = max(i for i in range(10, 0, -1) if A[i] != 0)
    
    if maxx - minn <= 2:
        ans = max(ans, end_point - start_point + 1)
        end_point += 1
        if end_point < n:
            A[arr[end_point]] += 1

    else:
        A[arr[start_point]] -= 1
        start_point += 1

print(int(ans))

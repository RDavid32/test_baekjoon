n = int(input())
x, s = map(int, input().split())
arr = []
check = False
for _ in range(n):
    c, p = map(int, input().split())
    if not check and c <= x and p > s:
        check = True
        
if check:
    print("YES")
else:
    print("NO")
        
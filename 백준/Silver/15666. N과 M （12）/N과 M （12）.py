import sys
input = sys.stdin.readline
def nm(a, start,ans):
    if a == m:
        print(*ans)
        return

    for i in range(start, len(arr)):
        ans.append(arr[i])
        nm(a+1, i,ans)
        ans.pop()

n, m = map(int, input().split())
arr = sorted(set(list(map(int, input().split()))))
ans = []

nm(0, 0,ans)

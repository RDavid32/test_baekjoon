import sys
input = sys.stdin.readline
def DFS(idx, cnt) :
    visit[idx] = 1
    for i in arr[idx] :
        if visit[i] == 0 :
            cnt = DFS(i, cnt+1)

    return cnt
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    for q in range(m):
        a, b = map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    visit = [0] * (n+1)
    print(DFS(1,0))
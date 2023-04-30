import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * n
result = []

def dfs():
    if len(result) == m:
        print(*result)
        return
    check = 0
    
    for q in range(n):
        if not visited[q] and check != num[q]:
            visited[q] = True
            result.append(num[q])
            check = num[q]
            dfs()
            visited[q] = False
            result.pop()

dfs()
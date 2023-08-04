
import sys
input = sys.stdin.readline

def dfs(check):
    if visited[check]:
        return False
    visited[check] = True
    
    for q in cow[check]:
        if not result[q] or dfs(result[q]):
            result[q] = check
            return True
            
    return False

n,m = map(int,input().split())
cow = [[] for _ in range(n+1)]
result = [0 for _ in range(m+1)]
for q in range(1,n+1):
    a,*b = map(int,input().split())
    cow[q] = b
for q in range(1,n+1):
    visited = [False for _ in range(n+1)]
    dfs(q)

print(sum([1 for i in result if i > 0]))
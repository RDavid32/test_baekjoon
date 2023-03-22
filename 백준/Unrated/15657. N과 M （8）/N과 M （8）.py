import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
result = []

check = list(map(int,input().split()))
check.sort()
def dfs(start):
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in range(start,len(check)):

            result.append(check[i])
            dfs(i)
            result.pop()
            
dfs(0)
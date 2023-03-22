import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))
result = []

check = list(map(int,input().split()))
check.sort()
def dfs():
    if len(result)==m:
        print(' '.join(map(str,result)))
        return
    
    for i in check:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
            
dfs()
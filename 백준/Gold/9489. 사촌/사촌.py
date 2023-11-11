import sys
input = sys.stdin.readline
from collections import defaultdict


while True:
    n,k = map(int,input().split())
    if n == k == 0:
        break
    arr = list(map(int,input().split()))
    parents = defaultdict(int)
    idx=0
    
    for q in range(1,n):
        parents[arr[q]] = arr[idx]
        if q <n-1 and arr[q]+1 < arr[q+1]:
            idx+=1
        
    if parents[parents[k]]:
        result=0
        for node in arr:
            if (parents[parents[k]] == parents[parents[node]]) and (parents[k] != parents[node]):
                result+=1
        print(result)
    else:
        print(0)

from collections import deque
import sys
input = sys.stdin.readline 
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(set,input().strip().split(' ')))
    
    if n > 32:
        result = 0
    else:
        result = 100000
        for q in range(n-2):
            for w in range(q+1,n-1):
                for e in range(w+1,n):
                    result = min(result, len(arr[q] | arr[w]) + len(arr[w]| arr[e]) + len(arr[e]| arr[q]) - 12) 
    print(result)
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int,input().split()) 
    odder = [0 for _ in range(n+1)] 
    time = [0] + list(map(int,input().split()))
    arr = [[] for _ in range(n+1)] 
    dp = [0 for _ in range(n+1)]
    
    for q in range(k):
        x,y = map(int,input().split())
        arr[x].append(y)
        odder[y] +=1

    queue = deque()
    for q in range(1, n+1):
        if odder[q] == 0:
            queue.append(q)
            dp[q] += time[q]
            
    while queue:
        a = queue.popleft()
        for q in arr[a]:
            odder[q] -= 1
            dp[q] =max(dp[a]+ time[q],dp[q])
            if odder[q] == 0:
                queue.append(q)
            
    w = int(input())
    print(dp[w])

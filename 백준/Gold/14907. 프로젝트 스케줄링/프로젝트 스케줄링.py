from heapq import heappop, heappush
import sys
input = sys.stdin.readlines()

time_arr = {}
next = [[] for _ in range(26)]
in_degree = [0] * 26
dp = [0 for _ in range(26)]

for q in input:
    check = q.split()
    name = ord(check[0])-65

    if len(check) == 2:
        time_arr[name] = int(check[1])

    else:
        time_arr[name] = int(check[1])
        in_degree[name] += len(check[2])

        for i in check[2]:
            next[ord(i)-65].append(name)
start = []

for i in time_arr:
    if not in_degree[i]:
        heappush(start, i)
        dp[i] = time_arr[i]
    
while start:
    x = heappop(start)

    for i in next[x]:
        in_degree[i] -= 1
        dp[i] = max(dp[x] + time_arr[i], dp[i])

        if not in_degree[i]:
            heappush(start, i)
            
print(max(dp))
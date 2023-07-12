import sys, math
input =sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(max(math.lcm(n,n-1,n-2), math.lcm(n,n-1,n-3), math.lcm(n-1,n-2,n-3)))
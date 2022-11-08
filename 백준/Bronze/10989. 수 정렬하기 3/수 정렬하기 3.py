import sys

N = int(input())

z = [0] * 10001

for i in range(N):
    s = int(sys.stdin.readline())
    
    z[s] = z[s] + 1
    
for i in range(10001):
    if z[i] != 0:
        for j in range(z[i]):
            print(i)
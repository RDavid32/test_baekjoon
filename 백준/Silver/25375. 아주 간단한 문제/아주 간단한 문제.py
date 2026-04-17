import sys

n = int(input())
for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    if b % a == 0 and b // a >= 2 :
        print(1)
    else:
        print(0)
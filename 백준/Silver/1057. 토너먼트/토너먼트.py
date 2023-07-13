import sys
input =sys.stdin.readline
n,a,b = map(int,input().split())
check = 0

while a != b:
    a -= a//2
    b -= b//2
    check += 1
print(check)
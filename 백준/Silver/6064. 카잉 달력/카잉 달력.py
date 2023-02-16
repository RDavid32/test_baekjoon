import sys
input = sys.stdin.readline

t = int(input())

for q in range(t):
    check =0
    m, n, x, y = map(int, input().split())
    while x <= m * n:
        if (x - y) % n == 0:
            print(x)
            check = 1
            break
        x += m
    if check == 0:
        print(-1)


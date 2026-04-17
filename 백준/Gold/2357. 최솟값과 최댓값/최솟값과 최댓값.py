import sys
input = sys.stdin.readline
n, m = map(int,input().split())

tree = [[0, 0] for _ in range(n << 1)]

def update(i, val):
    i += n
    tree[i][0] = val
    tree[i][1] = val
    while i >> 1:
        i >>= 1
        tree[i][0] = max(tree[i << 1][0], tree[i << 1 | 1][0])
        tree[i][1] = min(tree[i << 1][1], tree[i << 1 | 1][1])

def solve(l, r):
    max_num = 0
    min_num = 10e9
    l += n
    r += n
    while l <= r:
        if l & 1:
            max_num = max(tree[l][0], max_num)
            min_num = min(tree[l][1], min_num)
            l += 1
        if not (r & 1):
            max_num = max(tree[r][0], max_num)
            min_num = min(tree[r][1], min_num)
            
            r -= 1
        l >>= 1
        r >>= 1
    return min_num, max_num

for i in range(n):
    num = int(input())
    update(i, num)

for _ in range(m):
    left, right= map(int,input().split())
    print(*solve(left-1, right-1))
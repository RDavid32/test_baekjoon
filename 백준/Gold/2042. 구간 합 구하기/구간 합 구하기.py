import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())

tree = [0] * (n << 1)

def update(i, val):
    i += n
    tree[i] = val
    while i >> 1:
        i >>= 1
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

def get_sum(l, r):
    total = 0
    l += n
    r += n
    while l <= r:
        if l & 1:
            total += tree[l]
            l += 1
        if not (r & 1):
            total += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return total

for i in range(n):
    num = int(input())
    update(i, num)

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(get_sum(b-1, c-1))
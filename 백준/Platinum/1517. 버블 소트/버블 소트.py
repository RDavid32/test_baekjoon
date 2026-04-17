import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

comp = {v: i for i, v in enumerate(sorted(set(arr)))}

tree = [0] * (n << 1)

def update(i, val):
    i += n
    tree[i] += val
    while i > 1:
        i >>= 1
        tree[i] = tree[i << 1] + tree[i << 1 | 1]

def solve(l, r):
    if l > r:
        return 0
    result = 0
    l += n
    r += n
    while l <= r:
        if l & 1:
            result += tree[l]
            l += 1
        if not (r & 1):
            result += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    return result

result = 0

for x in arr:
    idx = comp[x]
    result += solve(idx + 1, n - 1)
    update(idx, 1)

print(result)
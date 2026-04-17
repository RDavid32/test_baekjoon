import sys
input = sys.stdin.readline

MOD = 10**9 + 7

n = int(input())
arr = list(map(int, input().split()))

size = 1
while size < n:
    size <<= 1

tree = [0] * (size << 1)
length = [0] * (size << 1)

lazy_mul = [1] * (size << 1)
lazy_add = [0] * (size << 1)

lazy_set = [0] * (size << 1)
has_set = [False] * (size << 1)

for i in range(size, size + n):
    length[i] = 1
for i in range(size - 1, 0, -1):
    length[i] = length[i << 1] + length[i << 1 | 1]

for i in range(n):
    tree[size + i] = arr[i] % MOD
for i in range(size - 1, 0, -1):
    tree[i] = (tree[i << 1] + tree[i << 1 | 1]) % MOD

height = size.bit_length()


def apply_set(node, val):
    val %= MOD
    tree[node] = (val * length[node]) % MOD
    if node < size:
        has_set[node] = True
        lazy_set[node] = val
        lazy_mul[node] = 1
        lazy_add[node] = 0


def apply(node, mul, add):
    mul %= MOD
    add %= MOD

    tree[node] = (tree[node] * mul + add * length[node]) % MOD

    if node < size:
        if has_set[node]:
            lazy_set[node] = (lazy_set[node] * mul + add) % MOD
        else:
            lazy_mul[node] = (lazy_mul[node] * mul) % MOD
            lazy_add[node] = (lazy_add[node] * mul + add) % MOD


def push(node):
    if has_set[node]:
        apply_set(node << 1, lazy_set[node])
        apply_set(node << 1 | 1, lazy_set[node])
        has_set[node] = False

    if lazy_mul[node] != 1 or lazy_add[node] != 0:
        apply(node << 1, lazy_mul[node], lazy_add[node])
        apply(node << 1 | 1, lazy_mul[node], lazy_add[node])
        lazy_mul[node] = 1
        lazy_add[node] = 0


def push_path(node):
    for h in range(height, 0, -1):
        x = node >> h
        if x:
            push(x)


def pull(node):
    while node > 1:
        node >>= 1
        tree[node] = (tree[node << 1] + tree[node << 1 | 1]) % MOD

        if has_set[node]:
            tree[node] = (lazy_set[node] * length[node]) % MOD

        if lazy_mul[node] != 1 or lazy_add[node] != 0:
            tree[node] = (tree[node] * lazy_mul[node] + lazy_add[node] * length[node]) % MOD


def range_update(l, r, mul, add):

    l += size
    r += size + 1

    l0 = l
    r0 = r - 1

    push_path(l0)
    push_path(r0)

    left = l
    right = r

    while left < right:
        if left & 1:
            apply(left, mul, add)
            left += 1
        if right & 1:
            right -= 1
            apply(right, mul, add)
        left >>= 1
        right >>= 1

    pull(l0)
    pull(r0)


def range_set(l, r, val):

    l += size
    r += size + 1

    l0 = l
    r0 = r - 1

    push_path(l0)
    push_path(r0)

    left = l
    right = r

    while left < right:
        if left & 1:
            apply_set(left, val)
            left += 1
        if right & 1:
            right -= 1
            apply_set(right, val)
        left >>= 1
        right >>= 1

    pull(l0)
    pull(r0)


def range_add(l, r, val):
    range_update(l, r, 1, val)


def range_mul(l, r, val):
    range_update(l, r, val, 0)


def range_sum(l, r):
    l += size
    r += size + 1

    push_path(l)
    push_path(r - 1)

    res = 0
    while l < r:
        if l & 1:
            res = (res + tree[l]) % MOD
            l += 1
        if r & 1:
            r -= 1
            res = (res + tree[r]) % MOD
        l >>= 1
        r >>= 1

    return res


m = int(input())
for _ in range(m):
    q = list(map(int, input().split()))

    if q[0] == 1:
        _, x, y, v = q
        range_add(x - 1, y - 1, v)
    elif q[0] == 2:
        _, x, y, v = q
        range_mul(x - 1, y - 1, v)
    elif q[0] == 3:
        _, x, y, v = q
        range_set(x - 1, y - 1, v)
    else:
        _, x, y = q
        print(range_sum(x - 1, y - 1))
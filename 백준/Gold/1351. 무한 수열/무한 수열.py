from collections import defaultdict
import sys

def dd(n):
    if a_1[n] != 0:
        return a_1[n]
    a_1[n] = dd(n // p) + dd(n // q)
    return a_1[n]

n, p, q = map(int, sys.stdin.readline().split())
a_1 = defaultdict(int)
a_1[0] = 1
print(dd(n))
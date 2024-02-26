import math
import sys
input = sys.stdin.readline
n, m = map(int,input().split())

check = math.gcd(n,m)
result = '1'*check
print(result)
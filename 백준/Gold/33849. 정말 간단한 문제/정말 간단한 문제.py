import sys
import math

input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

g = gcd(A[0], B[0])
prevA = A[0] // g
prevB = B[0] // g

result = 1
mx = -10**9 + 7

for i in range(1, n):
    g = gcd(A[i], B[i])
    A[i] //= g
    B[i] //= g

    if prevA * B[i] == prevB * A[i]:
        result += 1
    elif prevA * B[i] > prevB * A[i]:
        result = 1
        mx = 0
        prevA = A[i]
        prevB = B[i]
    else:
        mx = max(mx, result)
        result = 0

if prevA * B[-1] == prevB * A[-1]:
    mx = max(mx, result)

print(prevB, prevA)
print(mx)

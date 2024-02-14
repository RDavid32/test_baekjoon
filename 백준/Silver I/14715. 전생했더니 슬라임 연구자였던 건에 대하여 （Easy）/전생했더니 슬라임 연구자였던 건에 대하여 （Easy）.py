import math
import sys

K = int(sys.stdin.readline())
cnt = 1

while True:
    isPrime = True
    for i in range(2, int(math.sqrt(K)) + 1):
        if K % i == 0:
            isPrime = False
            K //= i
            cnt += 1
            break

    if isPrime:
        break

ans = math.ceil(math.log10(cnt) / math.log10(2))
print(ans)

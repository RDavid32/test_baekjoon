import sys
from collections import deque

input = sys.stdin.readline

def dp(a, b):
    queue = deque([(a, 1)])

    while queue:
        num, count = queue.popleft()

        if num == b:
            print(count)
            return

        if num * 2 <= b:
            queue.append((num * 2, count + 1))

        if num * 10 + 1 <= b:
            queue.append((num * 10 + 1, count + 1))

    print(-1)


a, b = map(int, input().split())
dp(a, b)
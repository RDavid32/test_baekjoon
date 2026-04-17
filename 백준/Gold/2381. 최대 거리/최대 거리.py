import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]

max_plus = -1e9
min_plus = 1e9
max_minus = -1e9
min_minus = 1e9

for x, y in nums:
    max_plus = max(max_plus, y + x)
    min_plus = min(min_plus, y + x)

    max_minus = max(max_minus, y - x)
    min_minus = min(min_minus, y - x)

print(max(max_plus - min_plus, max_minus - min_minus))
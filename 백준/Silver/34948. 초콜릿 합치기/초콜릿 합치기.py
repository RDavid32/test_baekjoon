N = int(input())

H = list(map(int, input().split()))
W = list(map(int, input().split()))

heights = []

for i in range(N):
    heights.append([H[i], W[i]])

heights.sort(reverse=True)

check = 0
result = 0

for i, j in heights:
    check += j
    area = i * check
    result = max(result, area)

print(result)
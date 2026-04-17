import sys
input = sys.stdin.readline

def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

t = int(input())

for q in range(1, t+1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    lis = [numbers[0]]
    for i in range(1, n):
        if lis[-1] < numbers[i]:
            lis.append(numbers[i])
        else:
            j = binary_search(0, len(lis)-1, numbers[i])
            lis[j] = numbers[i]

    print(f'Case #{q}')
    if len(lis) >= k:
        print(1)
    else:
        print(0)
import sys
input = sys.stdin.readline

def solve(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            left_check = arr[left + 1 : right + 1]
            if left_check == left_check[::-1]:
                return 1
            right_check = arr[left : right]
            if right_check == right_check[::-1]:
                return 1
            return 2
        left += 1
        right -= 1
    return 0




n = int(input())

for _ in range(n):
    arr = list(input().strip())
    print(solve(arr))
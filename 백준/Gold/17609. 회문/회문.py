import sys
input = sys.stdin.readline


def palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def solve(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            if palindrome(s, left + 1, right):
                return 1
            if palindrome(s, left, right - 1):
                return 1
            return 2
        left += 1
        right -= 1

    return 0


n = int(input())

for _ in range(n):
    s = input().strip()
    print(solve(s))
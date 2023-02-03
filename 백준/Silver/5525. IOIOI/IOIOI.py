from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
answer = 0
q = 0 
count = 0

while q < (m - 1):
    if s[q:q+3] == 'IOI':
        q += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        q += 1
        count = 0

print(answer)
import sys
input = sys.stdin.readline

n = int(input())
arr = input().strip()
stack = []
counter = [0 for _ in range(n)]

for q in range(n):
    if arr[q] == '(':
        stack.append(q)
    else:
        if stack:
            counter[q] = counter[stack[-1]] = 1
            stack.pop()

answer = 0
count = 0
for number in counter:
    if number == 1:
        count += 1
        answer = max(answer, count)
    else:
        count = 0
print(answer)
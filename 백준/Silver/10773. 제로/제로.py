n = int(input())
stack = []
answer = []
count = 0

for q in range(n):
    a = int(input())
    if a != 0:
        stack.append(a)
    else:
        del stack[-1]
print(sum(stack))

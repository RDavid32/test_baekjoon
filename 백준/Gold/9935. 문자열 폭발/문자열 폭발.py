arr = list(input())
bombworld = list(input())
bombworldlen = len(bombworld)

stack = []
for q in arr:
    stack.append(q)
    if stack[len(stack) - bombworldlen: len(stack)] == bombworld:
        for _ in range(bombworldlen):
            stack.pop()

if stack:
    print(*stack, sep = '')
else:
    print("FRULA")
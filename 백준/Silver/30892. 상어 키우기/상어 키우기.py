n, k, t = map(int,input().split())
sharks = list(map(int,input().split()))
sharks.sort()

stack = []

for i in range(n):
    if k == 0:
        break

    if sharks[i] < t:
        stack.append(sharks[i])
    else:
        while stack and sharks[i] >= t and k > 0:
            t += stack.pop()
            k -= 1

        if sharks[i] < t:
            stack.append(sharks[i])
        else:
            break

while k > 0 and stack:
    t += stack.pop()
    k -= 1

print(t)
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int,input().split()))
code = []
answer = 0

for i in range(k):
    if arr[i] in code :  
        continue

    if len(code) < n :  
        code.append(arr[i])
        continue

    check = []
    for j in code:  
        if j in arr[i:]: 
            check.append(arr[i:].index(j))
        else:
            check.append(101)
    idx = check.index(max(check))
    code.remove(code[idx])
    code.append(arr[i])
    answer += 1

print(answer)
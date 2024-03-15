def change(num):
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] = 0

arrlen = int(input())
arr = [-1] + list(map(int, input().split()))
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    if a == 1:
        for i in range(b, arrlen+1, b):
            change(i)

    else:
        change(b)
        for k in range(arrlen//2):
            if b + k > arrlen or b - k < 1 : break
            if arr[b + k] == arr[b - k]:
                change(b + k)
                change(b - k)
            else:
                break
                
for i in range(1, arrlen+1):
    print(arr[i], end = " ")
    if i % 20 == 0 :
        print()
n = int(input())
arr = [0 for _ in range(10)]
check = 1
while n != 0:
    while n % 10 != 9:
        for i in str(n):
            arr[int(i)] += check
        n -= 1
    if n < 10:
        for i in range(n + 1):
            arr[i] += check
        arr[0] -= check
        break
    else:
        for i in range(10):
            arr[i] += (n // 10 + 1) * check
    arr[0] -= check
    check *= 10
    n //= 10

print(sum(arr) % 1234567)
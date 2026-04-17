n = int(input())
count = [0 for _ in range(10)]
num = 1
def make_nine(N):
    while N % 10 != 9:
        for i in str(N):
            count[int(i)] += num
        N -= 1
    return N

while n > 0:
    n = make_nine(n)
    if n < 10:
        for i in range(n + 1):
            count[i] += num
            
    else:
        for i in range(10):
            count[i] += (n // 10 + 1) * num
    count[0] -= num
    num *= 10
    n //= 10

print(*count)
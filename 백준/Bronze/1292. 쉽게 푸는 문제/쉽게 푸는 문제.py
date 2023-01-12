N, M = map(int, input().split())
num = [0]
count = 1

for i in range(1, (M+1) // 2 + 1):
    for j in range(count):
        num.append(count)
    count += 1
 
for i in range(1, M+1):
    num[i] += num[i-1]

print(num[M] - num[N-1])
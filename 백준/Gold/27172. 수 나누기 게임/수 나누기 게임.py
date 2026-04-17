n = int(input())
arr= list(map(int, input().split()))

arr_nums = set(arr)
max_num = max(arr_nums)

result = [0 for _ in range(max_num + 1)]
for i in arr:
    if i == max_num:
        continue
    for j in range(2 * i, max_num + 1, i):
        if j in arr_nums:
            result[i] += 1
            result[j] -= 1

for i in arr:
    print(result[i], end=' ')
import sys
input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n)]
for q in range(n):
    arr[q] = list(map(int,input().split())) 

arr.sort(key = lambda x:x[0])

result = 0

min_num = arr[0][0]
max_num = arr[0][1]

for q,w in arr[1:]:
    if q > max_num:
        result += max_num - min_num
        min_num = q
        max_num = w
    
    else:
        max_num = max(w, max_num)

print(result + (max_num - min_num))
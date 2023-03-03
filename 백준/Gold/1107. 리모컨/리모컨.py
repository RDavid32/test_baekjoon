import sys
input = sys.stdin.readline

button = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_num = abs(100 - button)

for num in range(1000001):
    num = str(num)
    
    for q in range(len(num)):
       
        if int(num[q]) in broken:
            break

        elif q == len(num) - 1:
            min_num = min(min_num, abs(int(num) - button) + len(num))

print(min_num)
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for i in range(n):
    number = int(sys.stdin.readline())
    num_list[number] += 1

for i in range(10001):
    for j in range(num_list[i]):
        print(i)
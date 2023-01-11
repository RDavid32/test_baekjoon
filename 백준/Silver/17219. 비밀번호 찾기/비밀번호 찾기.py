import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for q in range(1, N + 1):
    a,b = input().rstrip().split()
    dict[a] =b
for w in range(M):
    site = input().rstrip()
    print(dict[site])
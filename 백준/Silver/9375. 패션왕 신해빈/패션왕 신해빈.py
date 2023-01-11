import sys
input = sys.stdin.readline

N = int(input())
for w in range(N):
    dict = {}
    M = int(input())
    result =1
    for q in range(1, M + 1):
        a,b = input().rstrip().split()
        if b in dict:
            dict[b] = dict[b]+1
        else:
            dict[b] =1
    for q in dict.values():
        result*=q+1
    print(result-1)
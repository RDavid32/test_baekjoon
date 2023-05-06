import sys
input =sys.stdin.readline

N = int(input())
card=list(map(int,input().split()))
M = int(input())
finds =list(map(int,input().split()))

dic={}

for q in card:
    if q in dic:
        dic[q] +=1
    else:
        dic[q] =1

for q in finds:
    if q in dic:
        print(dic[q],end=" ")
    else:
        print(0,end=" ")
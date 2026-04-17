import sys
input = sys.stdin.readline

n = int(input())
villages = []
people=0
for _ in range(n):
    pos, peo = map(int, input().split())
    villages.append((pos, peo))
    people += peo
    
villages.sort(key=lambda x : x[0])

count = 0
for pos, peo in villages:
    count+=peo
    if count>=(people/2):
        print(pos)
        break
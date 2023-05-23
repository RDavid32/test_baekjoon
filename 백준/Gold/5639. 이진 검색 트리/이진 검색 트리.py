import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

result = []
while True:
    try:
        result.append(int(input()))
    except:
        break

def go(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if result[i] > result[start]:
            mid = i
            break
    go(start + 1, mid - 1)
    go(mid, end) 
    print(result[start]) 

go(0, len(result) - 1)
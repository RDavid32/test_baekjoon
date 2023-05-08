import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, b, c = map(int,input().split())
    ab, bc, ca = map(int,input().split())
    result =0
    money = 0
    for abnum in range(min(a,b)+1):
        bcnum = min(b-abnum,c)
        canum = min(c-bcnum,a-abnum)
        result = max(result, ab*abnum + bc*bcnum + ca *canum)
        canum = min(c,a-abnum)
        bcnum = min(c-canum,b-abnum)
        result = max(result, ab*abnum + bc*bcnum + ca *canum)

        
    print(result)
import sys
input = sys.stdin.readline

table = [0 for _ in range(1000000)]
for q in range(1,1000000):
    for w in range(q, 1000000,q):
        table[w]+=q
    table[q] = abs(2*q - table[q])
t=0

while True:
    t+=1
    s =  list(map(int,input().split()))
    if s == [0,0,0]:
        break
    result = 0
    for q in range(s[0],s[1]+1):
        if table[q] <= s[2]:
            result+=1
    
    print(f"Test {t}: {result}")
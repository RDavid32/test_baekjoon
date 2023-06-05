import sys
input = sys.stdin.readline

x = []
y = []
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

x1,y1 = 0,0
for i in range(n):
    x1 += x[i] * y[i+1]
    y1 += y[i] * x[i+1]
    
print(round(abs((x1-y1)/2),1))


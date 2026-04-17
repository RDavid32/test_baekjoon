a, b  = map(int,input().split())
result = 1
for i in range(a,b+1):
    result *= (i**2 + i)//2
    result = result % 14579
print(result)
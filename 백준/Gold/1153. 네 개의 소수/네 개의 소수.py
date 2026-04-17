
n = int(input())


if n < 8:
    print(-1)
    exit()
elif n%2==1:
    result = [2,3]
    n-=5
else:
    result = [2,2]
    n-=4

prime =[False, False] + [True]*(1000001)
    
for i in range(2,n+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j]=False
            
for i in range(2,(n+1)//2+1):
    if prime[i] and prime[n-i]:
        
        print(*result, i ,n-i)
        exit()
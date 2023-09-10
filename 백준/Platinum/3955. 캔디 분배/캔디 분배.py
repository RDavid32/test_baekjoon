import sys
input = sys.stdin.readline

def extend_gcd(a, b, K):
    s0, s1, t0, t1 = 1, 0, 0 , 1
    while b!= 0: 
        q,w = a//b , a%b
        a = b
        b = w
        s,t  = s0 - q*s1, t0 - q*t1
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t

    t0 = (t0 % K + K) % K

    if a != 1 or t0 > 10**9:
        return 'IMPOSSIBLE'
    
    return t0


t = int(input())
for  _ in range(t):
    k, c = map(int,input().split())
    if c == 1 :
        if k + 1 > 10**9:
            print("IMPOSSIBLE")
        else:
            print(k+1)
        continue
    if k == 1:
        print(1)
        continue
    answer = extend_gcd(k,c,k)
    print(answer)
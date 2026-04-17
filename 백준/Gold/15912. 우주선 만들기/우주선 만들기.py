n = int(input())

w = [0]+list(map(int,input().split()))
e = [0]+list(map(int,input().split()))


dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
    dp[i] = w[i] * e[i] + dp[i-1];
    w_max = w[i]
    e_max = e[i]
    
    for j in range(i-1,-1,-1):
        w_max = max(w_max, w[j])
        e_max = max(e_max, e[j])
        dp[i] = min(dp[i], w_max * e_max + dp[j-1])
print(dp[-1])



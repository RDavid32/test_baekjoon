N, M = map(int,input().split())

friend = [[1001 for j in range(N)] for i in range(N)]

for q in range(M):
    a,b = map(int,input().split())
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1
for q in range(N):
    for w in range(N):
        for e in range(N):
            friend[w][e] = min(friend[w][e], friend[w][q] + friend[q][e])
result =0
for q in range(N-1):
    if sum(friend[result]) > sum(friend[q+1]):
        result = q+1
print(result+1)
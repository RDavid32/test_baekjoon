import sys
input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M, K = map(int,input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int,input().split()) #질량, 속력, 방향
    arr[r-1][c-1].append([m,s,d])
    

for _ in range(K):
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            if arr[y][x]:
                for i in arr[y][x]:
                    m, s, d = i
                    nx = (x + dx[d] * s) % N 
                    ny = (y + dy[d] * s) % N
                    new_arr[ny][nx].append(i)
    
    arr[:] = new_arr
    

    for x in range(N):
        for y in range(N):
            if len(arr[y][x]) >= 2:
                check = arr[y][x]
                nm = sum(i[0] for i in check) // 5
                arr[y][x] = []
                if not nm:
                    continue
                ns = sum(i[1] for i in check) // len(check)
                if all(n[2] % 2 == 0 for n in check) or all(n[2] % 2 == 1 for n in check):
                    for i in [0,2,4,6]:
                        arr[y][x].append([nm,ns,i])
                else:
                    for i in [1,3,5,7]:
                        arr[y][x].append([nm,ns,i])

    
result=0
for x in range(N):
    for y in range(N):
        if arr[y][x]:
            result += sum(i[0] for i in arr[y][x])

print(result)
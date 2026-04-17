n, m = map(int,input().split())
r, c, d = map(int,input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = [list(map(int,input().split())) for _ in range(n)]

answer = 0

while True:
    if arr[r][c] == 0:
        arr[r][c] = 2
        answer += 1

    moved = False

    for _ in range(4):
        d = (d + 3) % 4   
        nr = r + dx[d]
        nc = c + dy[d]

        if arr[nr][nc] == 0:
            r, c = nr, nc
            moved = True
            break

    if moved:
        continue

    back = (d + 2) % 4
    nr = r + dx[back]
    nc = c + dy[back]

    if arr[nr][nc] == 1:
        break
    else:
        r, c = nr, nc

print(answer)
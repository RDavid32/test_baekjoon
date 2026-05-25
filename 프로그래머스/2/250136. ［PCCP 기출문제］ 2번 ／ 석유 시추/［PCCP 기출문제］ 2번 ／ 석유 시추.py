def solution(land):
    from collections import deque
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    m = len(land[0])
    n = len(land)
    ground = [0 for _ in range(m)]
    vistied = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] and not vistied[i][j]:
                que= deque([[i, j]])
                vistied[i][j] = True
                check = set()
                count = 1
                while que:
                    y, x = que.popleft()
                    check.add(x)
                    for k in range(4):
                        ix = x + dx[k]
                        iy = y + dy[k]
                        if 0 <= ix < m and 0 <= iy < n and land[iy][ix] and not vistied[iy][ix]:
                            que.append([iy, ix])
                            count += 1
                            vistied[iy][ix] = True
                for k in list(check):
                    ground[k] += count
            
    return max(ground)
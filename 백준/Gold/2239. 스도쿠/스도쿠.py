# 행검사
def row(y, num):
    for x in range(9):
        if num == sdoku[y][x]:
            return False
    return True


def col(x, num):
    for i in range(9):
        if num == sdoku[i][x]:
            return False
    return True


def square(j, i, num):
    
    nx = (i // 3) * 3
    ny = (j // 3) * 3
    for i in range(3):
        for j in range(3):
            if sdoku[ny + i][nx + j] == num:
                return False
    return True


def dfs(depth):
    if depth >= len(zero_p):
        for i in range(9):
            print(''.join(map(str, sdoku[i])))
        exit()

    y, x = zero_p[depth]
    for i in range(1, 10):

        if row(y, i) and col(x, i) and square(y, x, i):
            sdoku[y][x] = i
            dfs(depth + 1)
            sdoku[y][x] = 0


sdoku = []
zero_p = []  
for i in range(9):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        if temp[j] == 0:
            zero_p.append((i, j)) 
    sdoku.append(temp)

dfs(0)
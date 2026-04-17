import math
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n // 2, n // 2

result = sum(sum(i) for i in arr)

count = 1
sign = 1
direction = -1 #방향
while True:

    for i in range(count): #가로 방향
        x = x + direction
        if x < 0 :
            print(result - sum(sum(q) for q in arr))
            exit()
        check = 0 #움직인 모래 총합
        current_value = arr[y][x]

        for _ in range(2): #위 아래 (sign을 기준으로)
            for j, k, l in ((-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01), (0, 2, 0.02)): #x, y
                if 0 <= x + j * -direction < n and 0 <= y + k * sign < n:
                    arr[y + k * sign][x + j * -direction] += math.floor(current_value * l)
                check += math.floor(current_value * l)
            sign *= -1
            
        if 0 <= x + direction * 2 < n:
            arr[y][x + direction * 2] += math.floor(current_value * 0.05)
        check += math.floor(current_value * 0.05)
        
        if 0 <= x + direction < n:
            arr[y][x + direction] += current_value - check

        arr[y][x] = 0


    for i in range(count): #세로 방향
        y = y - direction
        current_value = arr[y][x]

        check = 0
        for _ in range(2): #위 아래 (sign을 기준으로)   
            for k, j, l in ((1, 1, 0.1), (0, 1, 0.07), (-1, 1, 0.01), (0, 2, 0.02)): #x, y
                if 0 <= x + j * sign  < n and 0 <= y + k * -direction< n:
                    arr[y + k * -direction][x + j * sign] += math.floor(current_value * l)

                check += math.floor(current_value * l)
            sign *= -1
            
        if 0 <= y - direction * 2 < n:
            arr[y - direction * 2][x] += math.floor(current_value * 0.05)

        check += math.floor(current_value * 0.05)

        if 0 <= y-direction < n:
            arr[y - direction][x] += current_value - check

        arr[y][x] = 0


    direction =  -direction
    count += 1

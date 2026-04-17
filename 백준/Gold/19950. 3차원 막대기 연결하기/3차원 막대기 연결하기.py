x1, y1, z1, x2, y2, z2 = map(int, input().split())
n = int(input())
stick = list(map(int, input().split()))

stick.sort()
dist = ((x1 - x2)**2 + (y1-y2)**2 + (z1 - z2)**2)**(1/2)

if sum(stick) >= dist:
    long_stick = stick[-1]
    del stick[-1]
    if long_stick - sum(stick) <= dist:
        print('YES')
        exit()

print('NO')
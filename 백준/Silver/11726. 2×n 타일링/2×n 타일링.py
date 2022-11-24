N = int(input())
tile = [0,1,2]
for q in range(3,10001):
    tile.append(tile[q-1]+ tile[q-2])
print(tile[N]%10007)
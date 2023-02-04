array = []
for q in range(9):
    array.append(int(input()))

array.sort()

total = sum(array)


for q in range(len(array)):
    for w in range(q + 1, len(array)):
        if total - array[q] - array[w] == 100:
            for e in range(len(array)):
                if e == q or e == w:
                    pass
                else:
                    print(array[e])
            exit()
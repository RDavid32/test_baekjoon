n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

def num(i, j): 
    return (i + 1) + n * j

answer = []

if n == 1:
    j = 0
    while j < m:
        if arr[0][j] == 'X':
            if j + 1 < m and arr[0][j + 1] == 'X':
                answer.append(f"2 {num(0, j)} {num(0, j + 1)}")
                j += 2
            else:
                answer.append(f"1 {num(0, j)}")
                j += 1
        else:
            j += 1
else:
    for j in range(m):
        i = 0
        while i < n:
            if arr[i][j] == 'X':
                if i + 1 < n and arr[i + 1][j] == 'X':
                    answer.append(f"2 {num(i, j)} {num(i + 1, j)}")
                    i += 2
                else:
                    answer.append(f"1 {num(i, j)}")
                    i += 1
            else:
                i += 1

print(len(answer))
for i in answer:
    print(i)
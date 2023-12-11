import sys
input = sys.stdin.readline
n = int(input())
result = 0
visited = [0] * n

def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == abs(x - i):
            return False
    
    return True

def NQueen(x):
    global result
    if x == n:
        result += 1
        return

    else:
        for y in range(n):
            visited[x] = y
            if check(x):
                NQueen(x+1)
           
NQueen(0)     
print(result)
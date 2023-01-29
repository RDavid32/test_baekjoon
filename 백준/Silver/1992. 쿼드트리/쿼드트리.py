import sys
input = sys.stdin.readline

def cut(x,y,n):
    color = tree[x][y]
    for q in range(x, x+n):
        for w in range(y, y+n):
            if tree[q][w] != color:
                n1 = n//2
                result.append('(')
                cut(x,y,n1)
                cut(x,y+n1,n1)
                cut(x+n1,y,n1)
                cut(x+n1,y+n1,n1)
                result.append(')')
                return
    if color == '1':
        result.append(1)
    else:
        result.append(0)

if __name__ == "__main__":
    n = int(input())

    tree = [0 for _ in range(n)]
    for q in range(n):
        tree[q] = list(input())
    
    x = 0
    y = 0
    result = []
    cut(x,y,n)

    for w in range(len(result)):
        print(result[w], end ="")

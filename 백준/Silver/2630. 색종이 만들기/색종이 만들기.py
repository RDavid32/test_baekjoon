import sys
input = sys.stdin.readline

def cut(x,y,n):
    color = paper[x][y]
    for q in range(x, x+n):
        for w in range(y, y+n):
            if paper[q][w] != color:
                n1 = n//2
                cut(x,y,n1)
                cut(x+n1,y,n1)
                cut(x,y+n1,n1)
                cut(x+n1,y+n1,n1)
                return
    if color == 0:
        result[0] +=1
    else:
        result[1]+=1

if __name__ == "__main__":
    n = int(input())

    paper = [0 for _ in range(n)]
    for q in range(n):
        paper[q] = list(map(int,input().split()))
    
    x = 0
    y = 0
    result = [0,0]

    cut(x,y,n)
    print(result[0])
    print(result[1])
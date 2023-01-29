import sys
input = sys.stdin.readline

def cut(x,y,n):
    color = paper[x][y]
    for q in range(x, x+n):
        for w in range(y, y+n):
            if paper[q][w] != color:
                n1 = n//3
                for e in range(3):
                    for r in range(3):
                        cut(x+n1*e,y+n1*r,n1)
                return
    if color == -1:
        result[0] +=1
    elif color == 0:
        result[1] +=1    
    else:
        result[2]+=1

if __name__ == "__main__":
    n = int(input())

    paper = [0 for _ in range(n)]
    for q in range(n):
        paper[q] = list(map(int,input().split()))
    
    x = 0
    y = 0
    result = [0,0,0]

    cut(x,y,n)
    print(result[0])
    print(result[1])
    print(result[2])
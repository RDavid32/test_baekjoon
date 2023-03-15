import sys      
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def shape(a,b,check,count):
    global result
    if count ==4: 
        result = max(check, result)
        return

    if check + max_num*(4-count) <= result:
        return
    
    for q in range(4):
        a1 = dx[q]+a
        b1 = dy[q]+b
        if 0<=a1 <n and 0<= b1<m and not visited[a1][b1]:

            if count == 2:
                visited[a1][b1] =True
                shape(a,b,check+paper[a1][b1],count+1)
                visited[a1][b1] = False
            
            visited[a1][b1] =True
            shape(a1,b1,check+paper[a1][b1],count+1)
            visited[a1][b1] = False


if __name__== "__main__":
    n, m = map(int,input().split())
    paper = []
    for q in range(n):
        paper.append(list(map(int,input().split())))
    max_num = max(map(max, paper)) 
    result = 0
    visited = [[False] * m for _ in range(n)]
    for q in range(n):
        for w in range(m):
            visited[q][w] = True
            shape(q,w,paper[q][w],1)
            visited[q][w] = False

    print(result)
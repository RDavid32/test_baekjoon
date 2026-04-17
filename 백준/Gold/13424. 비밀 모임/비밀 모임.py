import sys
input = sys.stdin.readline

INF = 1000001
for _ in range(int(input())):
    n, m = map(int,input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1,n+1):
        graph[i][i] = 0
    
    for i in range(m):
        a, b, c = map(int,input().split())
        graph[a][b] = c
        graph[b][a] = c
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                length = graph[j][i] + graph[i][k]
                if graph[j][k] > length:
                    graph[j][k] = length
                    graph[k][j] = length

    k = int(input())
    people = list(map(int,input().split()))
    total_road = INF*(n+1)
    result = 0
    for i in range(1,n+1):
        current_road = 0
        for node in people:
            current_road += graph[i][node]

        if current_road < total_road:
            result = i
            total_road = current_road
    print(result)
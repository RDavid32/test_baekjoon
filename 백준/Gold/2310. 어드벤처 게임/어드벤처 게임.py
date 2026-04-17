from collections import deque, defaultdict
def dfs(now, total_money):
    global flag, visited
    x = graph[now][0]
    money = int(graph[now][1])
    next_rooms = list(map(int, graph[now][2:-1]))

    if x == 'L':
        if total_money <= money:
            total_money = money
    elif x == "T":  
        if total_money >= money:
            total_money -= money
        else:
            return
    if now == n:
        flag = True
        return
    visited[now] = True 
    for next in next_rooms:
        if not visited[next]: 
            dfs(next, total_money)
    visited[now] = False 


while True:
    n = int(input())
    if n == 0:
        break
    graph = defaultdict(list)
    for i in range(n):
        temp = list(input().split())
        graph[i+1] = temp

    visited = [False] * (n+1)
    flag = False
    dfs(1, 0) 
    if flag:
        print("Yes")
    else:
        print("No")
    
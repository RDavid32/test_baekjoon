from collections import deque

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for move in range(1,7):
            move = now+move
            
            if 0 < move <= 100 and not visited[move]:
       
                if move in lad.keys():
                    move = lad[move]

                if move in snack.keys():
                    move = snack[move]

                if not visited[move]:
                    queue.append(move)
                    visited[move] = True
                    board[move] = board[now] + 1



if __name__ == '__main__':
    N, M = map(int,input().split())
    board = [0] * 101
    visited = [False] * 101

    snack = dict()
    lad = dict()
    for _ in range(N):
        q,w = map(int,input().split())
        lad[q] = w
    for _ in range(M):
        q,w = map(int,input().split())
        snack[q] = w

    bfs()
    print(board[100])
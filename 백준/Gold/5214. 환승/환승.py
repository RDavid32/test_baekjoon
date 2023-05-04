from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue.append(0)
    visited[0] = 1
    while queue:
        x = queue.popleft()
        if x == n-1:
            print(visited[x])
            return
        for idx in tube[x]:
            if not visited[idx]:
                if idx >= n:
                    visited[idx] = visited[x]
                    queue.append(idx)
                else:
                    visited[idx] = visited[x] + 1
                    queue.append(idx)
    print(-1)
if __name__ == "__main__":
    n, k, m = map(int, input().split())
    tube = [[] for _ in range(n+m)]
    visited = [0 for _ in range(n+m)]
    queue = deque()


    for q in range(m):
        row = list(map(int, input().split()))
        for w in range(k):
            tube[row[w]-1].append(n+q)
            tube[n+q].append(row[w]-1)

    bfs()
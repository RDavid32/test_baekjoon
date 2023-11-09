from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def make_diamond_unit(i, j):
    global field, n, m
    if not (0 <= i < n and 0 <= j < m):
        return
    field[i][j] = -1

def make_diamond(ci, cj, cr):
    std_step = ((0, -1), (-1, 0), (0, 1), (1, 0))
    std_didj = ((-1, 1), (1, 1), (1, -1), (-1, -1))
    for idx in range(4):
        k = 0
        si, sj = std_step[idx]
        i, j = ci + si * cr, cj + sj * cr
        di, dj = std_didj[idx]
        while k <= cr:
            make_diamond_unit(i, j)
            i, j, k = i + di, j + dj, k + 1
            
def check_range():
    i, j, r = map(int, input().split())
    if i+j <= r: return False
    i, j = i-1, j-1
    make_diamond(i, j, r)
    return True

def bfs():
    while queue:
        x, y = queue.popleft()
        for q in range(4):
            x1 = x + dx[q]
            y1 = y + dy[q]
            if 0 <= x1 < n and 0 <= y1 < m and field[x1][y1] == 0:
                field[x1][y1] = field[x][y] + 1
                queue.append([x1, y1])

    return

queue = deque()
n, m = map(int, input().split())
k = int(input())
field = [[0 for _ in range(3001)] for _ in range(3001)]
def main():
    for _ in range(k):
        if not check_range(): return False

queue = deque()
queue.append([0, 0])
main()
bfs()
result = field[n - 1][m - 1]
if result > 0:
    print("YES")
    print(result)
else:
    print("NO")

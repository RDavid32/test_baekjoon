from collections import deque
def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        num = queue.popleft()
        if  num == k:
            print(number[k])
            break

        for x in (num-1, num+1, num*2):
            if 0 <= x <= 100000 and not number[x]:
                number[x] = number[num]+1
                queue.append(x)

if __name__ == "__main__":
    n ,k =map(int,input().split())
    number = [0 for _ in range(100001)]
    bfs()

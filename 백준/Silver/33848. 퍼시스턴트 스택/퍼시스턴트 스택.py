from collections import deque
import sys
input = sys.stdin.readline

que = deque([])
stack = deque([])
Q = int(input())
for _ in range(Q):
    num, *i = map(int,input().split())

    if num == 1:
        que.append(i[0])
        stack.append([False,i[0]])
    elif num == 2:
        a = que.pop()
        stack.append([True,a])
    elif num == 3:
        for i in range(i[0]):
            check, cancel_num = stack.pop()
            if check:
                que.append(cancel_num)
            else:
                que.pop()
    elif num == 4:
        print(len(que))
    else:
        if que:

            last_val = que.pop()
            print(last_val)
            que.append(last_val)
        else:
            print(-1)
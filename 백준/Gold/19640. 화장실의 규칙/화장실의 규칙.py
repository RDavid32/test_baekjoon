import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

N, M, K = map(int, input().split())
waiting, index = [deque() for _ in range(M)], 0

for q in range(N):
    D, H = map(int, input().split())
    line_num = index%M
    waiting[line_num].append((D*(-1), H*(-1), line_num, q+1))
    index += 1

result = PriorityQueue()
for index in range(M):
    if waiting[index]:
        next_people = waiting[index].popleft()
        result.put(next_people)

people, count = -1, 0
while people != (K+1):
    a, b, people_line, people = result.get()
    count += 1
    if waiting[people_line]:
        next_people = waiting[people_line].popleft()
        result.put(next_people)

print(count-1)

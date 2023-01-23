from heapq import heappop
from heapq import heappush
import sys
input = sys.stdin.readline
heap = []
n= int(input())

for q in range(n):
    x = int(input())
    if x == 0:
        if len(heap) :
            print(-heappop(heap))
            
        else:
            print(0)
    else:
        heappush(heap, -x)
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
heap = []
num_index = defaultdict(int)
for idx in range(N):
    num_index[nums[idx]] = idx
    heapq.heappush(heap, nums[idx])
count = 0

for idx in range(N):
    tmp = heapq.heappop(heap)
    if nums[idx] != tmp:
        tix = num_index[tmp]
        num_index[nums[idx]] = tix
        nums[idx], nums[tix] = nums[tix], nums[idx]
        count += 1
print(count)
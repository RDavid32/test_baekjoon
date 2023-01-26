import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())

    for q in range(t):
        max_heap, min_que =[], []
        k = int(input())
        visit = [False] * 1000001
        
        for w in range(k):
            que = input().split()
            
            if que[0] == 'I':
                heapq.heappush(min_que,(int(que[1]), w))
                heapq.heappush(max_heap,(int(que[1]) * -1, w))
                visit[w] = True
            
            else:
                if que[1] =='1':
                    while max_heap and not visit[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    
                    if max_heap:
                        visit[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                else:
                    while min_que and not visit[min_que[0][1]]: 
                        heapq.heappop(min_que) 
                    
                    if min_que:
                        visit[min_que[0][1]] = False 
                        heapq.heappop(min_que)

        while min_que and not visit[min_que[0][1]]:
            heapq.heappop(min_que)
        while max_heap and not visit[max_heap[0][1]]:
            heapq.heappop(max_heap)

        if min_que and max_heap:
            print(-max_heap[0][0], min_que[0][0])
        else:
            print('EMPTY')

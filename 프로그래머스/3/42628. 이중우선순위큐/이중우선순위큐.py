import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)
    
    for i, op in enumerate(operations):
        command, value = op.split()
        num = int(value)
        
        if command == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True         
        elif command == "D":
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    _, i_id = heapq.heappop(max_heap)
                    visited[i_id] = False
            
            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    _, i_id = heapq.heappop(min_heap)
                    visited[i_id] = False

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
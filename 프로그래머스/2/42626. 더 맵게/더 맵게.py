import heapq

def solution(scoville, k):
    heapq.heapify(scoville)

    answer = 0

    while scoville[0] < k:
        if len(scoville) < 2:
            return -1

        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a + b * 2)
        answer += 1

    return answer
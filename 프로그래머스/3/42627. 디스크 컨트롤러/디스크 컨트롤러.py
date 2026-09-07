import heapq

def solution(jobs):
    n = len(jobs)

    jobs = sorted((start, idx, length) for idx, (start, length) in enumerate(jobs))

    heap = []
    time = 0
    answer = 0
    i = 0
    count = 0

    while count < n:

        while i < n and jobs[i][0] <= time:
            start, idx, length = jobs[i]

            heapq.heappush(heap, (length, start, idx))
            i += 1

        if heap:
            length, start, idx = heapq.heappop(heap)

            time += length
            answer += time - start
            count += 1

        else:
            time = jobs[i][0]

    return answer // n
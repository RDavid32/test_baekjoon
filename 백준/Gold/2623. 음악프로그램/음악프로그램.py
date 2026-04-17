from collections import deque
n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    length, *edges = map(int, input().split())
    for i in range(length):
        for j in range(i + 1, length):
            graph[edges[i]].append(edges[j])
            indegree[edges[j]] += 1

answer = []
queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])

while queue:
    node = queue.popleft()
    answer.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)
            

if len(answer) == n:
    for node in answer:
        print(node)
else:
    print(0)
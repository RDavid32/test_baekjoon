def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    answer = n

    def dfs(node, parent):
        nonlocal answer

        count = 1

        for next_node in graph[node]:
            if next_node == parent:
                continue

            child_count = dfs(next_node, node)
            answer = min(answer, abs(child_count - (n - child_count)))
            count += child_count

        return count

    dfs(1, 0)

    return answer
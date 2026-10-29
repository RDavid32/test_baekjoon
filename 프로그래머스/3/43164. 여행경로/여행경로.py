from collections import defaultdict

def solution(tickets):
    airport = defaultdict(list)

    for start, end in tickets:
        airport[start].append(end)

    for destinations in airport.values():
        destinations.sort(reverse=True)

    stack = ["ICN"]
    route = []

    while stack:
        current = stack[-1]

        if airport[current]:
            stack.append(airport[current].pop())
        else:
            route.append(stack.pop())

    return route[::-1]
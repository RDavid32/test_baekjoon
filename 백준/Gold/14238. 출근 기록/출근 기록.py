from collections import deque

info  = {"A" : 0, "B": 0, "C" : 0}
dp = set()
for s in input():
    info[s] += 1
def dfs(a, b, c, arr, b_check, c_check):

    if (a, b, c) == (0, 0, 0):
        print(*arr, sep = "")
        exit()

    if (a, b, c, b_check, c_check) in dp:
        return

    if c and c_check <= 0:
        arr.append("C")
        dfs(a, b, c-1, arr, 0, 2)
        arr.pop()
        dp.add((a, b, c, b_check, c_check))
    if b and b_check <= 0:
        arr.append("B")
        dfs(a, b-1, c, arr, 1, max(c_check - 1, 0))
        arr.pop()
        dp.add((a, b, c, b_check, c_check))
    
    if a:
        arr.append("A")
        dfs(a-1, b, c, arr, 0, max(c_check - 1, 0))
        arr.pop()
        dp.add((a, b, c, b_check, c_check))

dfs(info["A"], info["B"], info["C"], deque([]), 0, 0)
print("-1")
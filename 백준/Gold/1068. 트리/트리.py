def dfs(num):
    global tree
    
    for i in tree[num]:
        dfs(i)
    del tree[num]


n = int(input())
arr = list(map(int,input().split()))
remove_node = int(input())

tree = {i : [] for i in range(n)}
for idx, value in enumerate(arr):
    if value == -1:
        continue
    else:
        tree[value].append(idx)

dfs(remove_node)
print(sum(1 for v in tree.values() if v == [] or v == [remove_node]))
def lotto(arr,idx, depth):
    if depth == 6:
        print(*arr)
        return
    for q in range(idx, k):
        arr.append(s[q])
        lotto(arr, q+1, depth+1)
        arr.pop()
    
while True:
    k, *s = map(int,input().split())
    if k == 0:
        break
    arr = []
    lotto(arr,0,0)
    print()
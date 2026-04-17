arr = list(input())

ksa = ["A", "K", "S"]
if arr[0] == ksa[len(arr)%3]:
    print((len(arr) - 1) * 2)
else:
    print(len(arr) * 2)
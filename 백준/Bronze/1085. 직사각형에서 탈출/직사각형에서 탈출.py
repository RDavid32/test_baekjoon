a = list(map(int, input().strip().split()))
a[2] -= a[0]
a[3] -= a[1]
print (min(a))
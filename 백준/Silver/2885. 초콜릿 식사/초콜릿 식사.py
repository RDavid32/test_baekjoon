k = int(input())
check = 0
size = 1 
count = 0
while size < k:
    size *= 2
    check += 1
while not k & 1:
    k = k >> 1
    count += 1
print(size, check - count)
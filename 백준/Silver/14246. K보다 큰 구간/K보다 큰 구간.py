import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
k = int(input())
start = 0 
end = 1

num = arr[0]
result = 0
while n > end:
    if num > k:
        num -= arr[start]
        start += 1
        check = 1
        result += n - end +1
    else:
        num += arr[end]
        end += 1
        check = 0 

while num > k :
    num -= arr[start]
    start+=1
    result +=1
    
print(result)
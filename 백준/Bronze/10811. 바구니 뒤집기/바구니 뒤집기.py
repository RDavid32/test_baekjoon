import sys
input = sys.stdin.readline
n, m = map(int, input().split())

basket = [i for i in range(1,n+1)]

for q in range(m):
    i,j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for q in range(n):
    print(basket[q], end = ' ')


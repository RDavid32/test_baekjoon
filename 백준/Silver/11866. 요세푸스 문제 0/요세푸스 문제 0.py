a, b = map(int,input().split())
list_a = [0] * a
num = b
print('<',end='')
for q in range(a):
    list_a[q] = q+1
while len(list_a)>1:
    if len(list_a)>=num:
        print(list_a.pop(num-1),end=', ')
        num+=(b-1)
    else:
        num-=len(list_a)
print (list_a[0],end='')
print('>')
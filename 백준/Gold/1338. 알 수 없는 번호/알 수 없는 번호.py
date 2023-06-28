A,B = map(int,input().split())


if A>B:
    A,B = B,A
 
X,Y = map(int,input().split())
result = []
check = True
if Y>=abs(X) or Y<0:
    check = False
if check:
    X = abs(X)
    value = X*(A//X)+Y
    while value<=B:
        if A<=value<=B:
            if result:
                check = False
                break
            result.append(value)
        value += X
if check and result:
    print(*result)
else:
    print('Unknwon Number')
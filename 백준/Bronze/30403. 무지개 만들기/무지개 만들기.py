n = int(input())

uwordList = ['r', 'o', 'y', 'g', 'b', 'i', 'v']
lwordList = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']

u = []
l = []

uSign = 0 
lSign = 0

ans = input()

for i in ans : 
    
    if i.isupper() : 
        l.append(i)
    elif i.islower() : 
        u.append(i)

if all(str in u for str in uwordList) : 
    uSign = 1

if all(str in l for str in lwordList) : 
    lSign = 1

if uSign and lSign: 
    print('YeS')
elif uSign: 
    print('yes')
elif lSign: 
    print('YES')
else : 
    print('NO!')
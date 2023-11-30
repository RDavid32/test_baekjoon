t = int(input())

for _ in range(t):
    l_arr = []
    r_arr = []
    arr = input()
    for i in arr:
        if i == '-':
            if l_arr: 
                l_arr.pop()
        elif i == '<':
            if l_arr:
                r_arr.append(l_arr.pop())
        elif i == '>':
            if r_arr:
                l_arr.append(r_arr.pop())
        else:
            l_arr.append(i)
    l_arr.extend(reversed(r_arr)) 
    print(''.join(l_arr))
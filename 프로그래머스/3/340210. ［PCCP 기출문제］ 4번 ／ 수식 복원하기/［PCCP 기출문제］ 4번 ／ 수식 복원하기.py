
    
def solution(expressions):
    plus = []
    minus = []
    x = []
    start_num = 0
    for i in expressions:
        a, sign, b, _ , c = i.split(" ")
        if c == "X":
            x.append([int(a),sign,int(b)])
            start_num = max(start_num, max(int(d) for n in (a, b) for d in n))
        else:
            start_num = max(start_num, max(int(d) for n in (a, b, c) for d in n))
            if sign == "+":
                plus.append([int(a), int(b), int(c)])
            
            else:
                minus.append([int(a), int(b), int(c)])


    def calulation(idx):
        for i in plus:
            a, b, c = change_num(i, idx)
            if a + b != c:
                return False
        for i in minus:
            a, b, c = change_num(i, idx)
            if a - b != c:
                return False
        return True
            
    def change_num(arr, idx):
        a, b, *c = arr
        a1 = (a // 100) * (idx ** 2) + ((a % 100) // 10) * idx + a % 10
        b1 = (b // 100) * (idx ** 2) + ((b % 100) // 10) * idx + b % 10
        if len(arr) > 2:
            c = int(c[0])
            c1 = (c // 100) * (idx ** 2) + ((c % 100) // 10) * idx + c % 10
            return a1, b1, c1
        return a1, b1
    def reverse_change_num(num, idx):
        v = ""
        for i in range(2,-1,-1):
            v += str(num // (idx ** i))
            num %= (idx ** i)
        return int(v)
    def solve(arr):
        a, sign, b = arr
        a1, b1 = change_num([a,b], check[0])
        if sign == "+":
            before = a1 + b1
        else:
            before = a1 - b1
        before = reverse_change_num(before,check[0])
        for i in check[1:]:
            a1, b1 = change_num([a,b], i)
            if sign == "+":
                c1 = a1 + b1
            else:
                c1 = a1 - b1
            c1 = reverse_change_num(c1, i)
            print(c1)
            if before != c1:
                return False
        return before
    
    check = []
    for i in range(start_num + 1, 10):
        if calulation(i):
            check.append(i)
    
    answer = []
    
    for i in x:
        result = solve(i)

        if result is not False:
            answer.append(" ".join(map(str,i)) + " = " + str(result))
        else:
            answer.append(" ".join(map(str,i)) + " = " + "?")

    return answer
import sys
input = sys.stdin.readline

math = list(input())

q= 0 
result = 0
num=0
num1 =0 
check =1
while q<=len(math)-1:
    if math[q].isdigit():
        num = int(math[q])
        while math[q+1].isdigit():
            num = num*10 + int(math[q+1])
            q+=1
        result += check * num
    if math[q] == '-':
        check = -1
    q+=1
print(result)
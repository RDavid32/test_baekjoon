import sys
input = sys.stdin.readline

check = 0
result = 0
grade = ["A+","A0","B+","B0","C+",'C0','D+','D0','P','F']
grade.reverse()

for q in range(20):
    _,a,b = input().split()
    if b != 'P':
        result += float(a) * grade.index(b) * 0.5
        check += float(a)

print(f'{result/check:6f}')
class xfrac:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self): 
        numerator, denominator = self.calculate_fraction()
        common_divisor = self.gcd(numerator, denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        return numerator, denominator

    def calculate_fraction(self):
        # 연분수 계산
        #분자, 분모
        numerator_a, denominator_a = self.get_fraction_parts(self.a)
        numerator_b, denominator_b = self.get_fraction_parts(self.b)
        numerator_c, denominator_c = self.get_fraction_parts(self.c)

        # 분모를 계산
        denominator = denominator_a * denominator_b * numerator_c

        # 분자를 계산
        numerator = numerator_a * denominator_b * numerator_c + denominator_a * numerator_b * denominator_c
        return numerator, denominator

    def get_fraction_parts(self, fraction_part):
        # 숫자 또는 xfrac 객체의 분자와 분모를 반환
        if isinstance(fraction_part, xfrac):
            return fraction_part.calculate_fraction()
        else:
            return fraction_part, 1

    def gcd(self, a, b):
        # 최대공약수 계산
        while b != 0:
            a, b = b, a % b
        return a


def parse(s):
    stack = []
    try:
        for token in s:
            if token == '(':
                stack.append([])
            elif token.isdigit():
                stack[-1].append(int(token))
            else:  
                if stack:
                    top = stack.pop()  

                    if stack == []:
                        stack.append(xfrac(*top))
                    else:
                        stack[-1].append(xfrac(*top))

                else:
                    exit(0)

        while True:
            if isinstance(stack[0], xfrac):
                return stack[0]
            stack = stack[0]
    except:
        print(-1)
        exit(0)

n = int(input())
s = input().strip().split()

result = parse(s)
print(*result.evaluate())

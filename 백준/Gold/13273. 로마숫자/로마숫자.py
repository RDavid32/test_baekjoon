
roma = ['I','V','X','L','C','D','M']

n = int(input())

for q in range(n):
    
    case = input()
    if case.isdigit():
        result = ''
        case = int(case)
        check = case // 1000
        result += 'M' * check 
        case -= 1000 * check
        for q in range(2,-1,-1):    
            check = 10 ** q
            if case - 9 * check >= 0:
                case -= 9 * check
                result += roma [2*q] + roma[2*q+2]
            if case - 5 * check >= 0:
                case -= 5 * check
                result += roma [2*q+1]
            if case - 4 * check >= 0:
                case -= 4 * check
                result += roma[2*q] + roma[2*q + 1]
            if case - 1 * check >= 0:
                check_num = case // check
                result += roma[2*q] * check_num
                case -= check_num * check
    else:
        result = 0
        case = list(case)
        check = 0
        idx = 7
        for q in case:
            check = roma.index(q)

            if check %2:
                result += 5 * (10 ** (check//2))
                
                if idx < check:
                    result -= 2 * (10 ** (idx//2))

            else:

                if idx < check:
                    result -= 2 * (10 ** (idx//2))

                result += (10 ** (check//2))
            idx = check
    print(result)
def fast_modular_exponentiation(base, exponent, mod):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

def calculate_expression(x, n):
    mod = 1000000007
    term1 = fast_modular_exponentiation(x, n, mod)
    term2 = fast_modular_exponentiation(x - 1, n, mod)

    result = (term1 - term2) % mod
    return result

n, x = map(int,input().split())
result = calculate_expression(x, n)
print(result)

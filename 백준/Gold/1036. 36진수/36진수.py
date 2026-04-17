def char_to_val(c):
    if c.isdigit():
        return int(c)
    return ord(c) - 55  

def val_to_char(v):
    if v < 10:
        return str(v)
    return chr(v + 55)

def to_base36(num):
    if num == 0:
        return "0"
    result = []
    while num > 0:
        result.append(val_to_char(num % 36))
        num //= 36
    return ''.join(reversed(result))


n = int(input())
numbers = [input().strip() for _ in range(n)]
k = int(input())

total_sum = 0

arr = [0] * 36

for s in numbers:
    length = len(s)
    for i, ch in enumerate(s):
        val = char_to_val(ch)
        power = length - i - 1
        weight = 36 ** power

        total_sum += val * weight
        arr[val] += (35 - val) * weight

arr.sort(reverse=True)

for i in range(k):
    total_sum += arr[i]

print(to_base36(total_sum))
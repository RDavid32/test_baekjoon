d = int(input())
n, m, k = map(int, input().split())

n2 = n % d
m2 = m % d

maxsize = (n + m + k) // d

casearr = [0 for _ in range(4)]
caseksize = [0 for _ in range(4)]

casearr[0] = n // d + m // d + k // d
caseksize[0] = k
casearr[1] = (n + (d - n2)) // d + m // d + (k - (d - n2)) // d
caseksize[1] = k - (d - n2)
casearr[2] = n // d + (m + (d - m2)) // d + (k - (d - m2)) // d
caseksize[2] = k - (d - m2)
casearr[3] = (n + (d - n2)) // d + (m + (d - m2)) // d + (k - (d - n2) - (d - m2)) // d
caseksize[3] = k - (d - n2) - (d - m2)

result = 0

for i in range(4):
    if caseksize[i] > result and casearr[i] == maxsize:
        result = caseksize[i]

print(result)

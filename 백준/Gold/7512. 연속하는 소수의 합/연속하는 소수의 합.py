import sys
input = sys.stdin.readline
max_num = 10000001

num = [True for _ in range(max_num)]

primes = []

for i in range(2, max_num):
    if num[i]:
        primes.append(i)
        for j in range(i+i, max_num, i):
            num[j] = False

count_prime = len(primes)


t = int(input())

for q in range(1, t+1):
    m = int(input())
    n = list(map(int, input().split()))
    n.sort(reverse = True)

    total = [[sum(primes[:i]), 0] for i in n]

    while True:
        if num[total[0][0]]:
            break

        total[0][0] -= primes[total[0][1]]
        total[0][1] += 1

        if total[0][1] >= count_prime - n[0] + 1:
            break

        total[0][0] += primes[total[0][1] + n[0] - 1]


    left = 1

    while True:
        if left == m:
            break

        if left == 0:
            while True:
                total[0][0] -= primes[total[0][1]]
                total[0][1] += 1

                if total[0][1] >= count_prime - n[0] + 1:
                    break

                total[0][0] += primes[total[0][1] + n[0] - 1]
                if num[total[0][0]]:
                    break

            left += 1
            continue

        if total[left][0] == total[0][0]:
            left += 1
            continue

        elif total[left][0] > total[0][0]:
            left = 0
            continue

        else:
            total[left][0] -= primes[total[left][1]]
            total[left][1] += 1

            if total[left][1] >= count_prime - n[left] + 1:
                break

            total[left][0] += primes[total[left][1] + n[left] - 1]


    print(f"Scenario {q}:")
    print(total[0][0])
    print()
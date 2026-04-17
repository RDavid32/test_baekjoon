n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if n == 2 :
    if 1 in arr:
        other = arr[0] if arr[1] == 1 else arr[1]
        
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        if is_prime(other):
            print("NO")
            exit()

    print("YES")
    print(2)
    print(arr[0], arr[1])
else:
    print("YES")
    print(2)
    print(arr[1], arr[2])
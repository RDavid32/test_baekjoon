import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
if a == 1:
    print(b*8)
elif a == 2:
    print(b//2*8+1 + b%2*6)
elif a == 3:
    print(b//2*8+2 + b%2*4)
elif a == 4:
    print(b//2*8+3 + b%2*2)
else:
    print(b*8+4)

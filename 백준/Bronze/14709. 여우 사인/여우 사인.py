n = int(input())

finger = set()

for _ in range(n):
    a, b = map(int, input().split())
    finger.add(tuple(sorted((a, b))))

fox = {(1,3), (1,4), (3,4)}

if finger == fox:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")
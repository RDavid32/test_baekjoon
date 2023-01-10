N , M = map(int,input().split())
see = set()
hear = set()

for q in range(N):
    see.add(input())
for w in range(M):
    hear.add(input())

result = sorted(list(see & hear))
print(len(result))

for e in result:
    print(e)
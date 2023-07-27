import sys
input = sys.stdin.readline

leftword = input().strip()
rightword = input().strip()
leftlen, rightlen = len(leftword), len(rightword)
dp = [[0] * (rightlen + 1) for _ in range(leftlen + 1)]

for q in range(1, leftlen + 1):
    for w in range(1, rightlen + 1):
        if leftword[q-1] == rightword[w-1]:
            dp[q][w] = dp[q-1][w-1] + 1
            
        else:
            dp[q][w] = max(dp[q-1][w], dp[q][w-1])
print(dp[-1][-1])
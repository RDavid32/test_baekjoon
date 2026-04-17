import sys
input = sys.stdin.readline

first_line_min = []  
first_line_max = []
second_line_min = []
second_line_max = []
third_line_min = []
third_line_max = []

N = int(input())
dp = []
for _ in range(N):
    dp.append(tuple(map(int, input().split())))

first_line_min.append(dp[0][0])
second_line_min.append(dp[0][1])
third_line_min.append(dp[0][2])
for i in range(1, N):
    first_line_min.append(min(first_line_min[i-1], second_line_min[i-1]) + dp[i][0])
    second_line_min.append(min(first_line_min[i-1], second_line_min[i-1], third_line_min[i-1]) + dp[i][1])
    third_line_min.append(min(second_line_min[i-1], third_line_min[i-1]) + dp[i][2])
total_min = min(first_line_min[N-1], second_line_min[N-1], third_line_min[N-1])

first_line_max.append(dp[0][0])
second_line_max.append(dp[0][1])
third_line_max.append(dp[0][2])
for i in range(1, N):
    first_line_max.append(max(first_line_max[i-1], second_line_max[i-1]) + dp[i][0])
    second_line_max.append(max(first_line_max[i-1], second_line_max[i-1], third_line_max[-1]) + dp[i][1])
    third_line_max.append(max(second_line_max[i-1], third_line_max[i-1]) + dp[i][2])
total_max = max(first_line_max[N-1], second_line_max[N-1], third_line_max[N-1])

print(total_max, total_min)
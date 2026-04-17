import sys

n = int(input())

arr = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    arr.append([sm * 100 + sd, em * 100 + ed])


arr.sort()

end_date = 301
count = 0

while (arr):

    if (end_date >= 1201 or arr[0][0] > end_date):
        break

    temp_end_date = -1

    for _ in range(len(arr)):
        if (arr[0][0] <= end_date):
            if (temp_end_date <= arr[0][1]):
                temp_end_date = arr[0][1]

            arr.remove(arr[0])

        else:
            break

    end_date = temp_end_date

    count += 1


if end_date < 1201:
    print(0)
else:
    print(count)
def solution(arr):
    answer = []
    check = arr[0]
    for i in arr[1:]:
        if i != check:
            answer.append(check)
            check = i
    answer.append(check)
    return answer
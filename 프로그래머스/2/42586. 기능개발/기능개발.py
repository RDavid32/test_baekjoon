import math
def solution(progresses, speeds):
    answer = []
    max_time = math.ceil((100 - progresses[0])/ speeds[0])
    check = 1
    for i, j in zip(progresses[1:], speeds[1:]):
        if math.ceil((100 - i)/j) <= max_time:
            check += 1
        else:
            answer.append(check)
            check = 1
            max_time = math.ceil((100 - i)/j)
    if math.ceil((100 - i)/j) <= max_time:
        answer.append(check)
    return answer
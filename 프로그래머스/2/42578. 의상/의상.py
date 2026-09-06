def solution(clothes):
    wear = {}
    for i, j in clothes:
        wear[j] = wear.get(j, []) + [i]
    
    answer = 1
    for i in wear.values():
        answer *= len(i) + 1
    return answer - 1
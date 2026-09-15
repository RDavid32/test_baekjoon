def solution(name):
    answer = 0
    n = len(name)
    for i in name:
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
    move = n - 1
    
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        move = min(move, 2 * i + n - next_idx)
        move = min(move,i + 2 * (n - next_idx))

    return answer + move
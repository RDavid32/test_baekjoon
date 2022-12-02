import sys
input = sys.stdin.readline

def solution(N, arr):
    arr.sort(reverse=True) 
    mx = arr[0] 
    answer = [arr.pop()] 
    while len(arr) > 0: 
        wait = []

        if answer[-1] + 1 == arr[-1]: 
            if arr[-1] == mx:
                idx = len(answer) - 1
                while idx >= 0 and answer[idx] == answer[-1]: 
                    idx -= 1
                answer = answer[:idx+1] + arr + answer[idx+1:]
                break

            else: 
                while answer[-1] + 1 == arr[-1]: 
                    wait.append(arr.pop())

        answer.append(arr.pop()) 
        arr += wait 

    return ' '.join([str(i) for i in answer])

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    result = solution(N, arr)
    print(result)


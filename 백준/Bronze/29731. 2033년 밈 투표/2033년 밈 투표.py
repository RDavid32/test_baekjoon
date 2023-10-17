# 입력 받기

N = int(input())

promises = []

for _ in range(N):

    promise = input()

    promises.append(promise)

# Rick Astley의 공약 정의

rick_astley_promise = [

    "Never gonna give you up",

    "Never gonna let you down",

    "Never gonna run around and desert you",

    "Never gonna make you cry",

    "Never gonna say goodbye",

    "Never gonna tell a lie and hurt you",

    "Never gonna stop"

]

# 공약 검사

def check_promises(promises):

    for promise in promises:

        if promise not in rick_astley_promise:

            return "Yes"

    return "No"

# 결과 출력

result = check_promises(promises)

print(result)


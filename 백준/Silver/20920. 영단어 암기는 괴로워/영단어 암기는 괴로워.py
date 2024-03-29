import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 단어 개수, 단어 길이
word_lst = {} 

for _ in range(N):
    word = input().strip()
    
    if len(word) < M:
        continue
    else: 
        if word in word_lst: 
            word_lst[word] += 1
        else:
            word_lst[word] = 1

word_lst = sorted(word_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수

for i in word_lst:
    print(i[0])
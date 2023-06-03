alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L = int(input())
alpha = list(input())
result=0
for q in range(L):
    result+=(alpha_list.index(alpha[q])+1)*(31**q)
print(result)
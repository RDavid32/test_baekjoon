from collections import deque
import sys
input = sys.stdin.readline
def front(node, result):
    result.append(node)   
    if tree[node][0] != '.':
        front(tree[node][0],result)

    if tree[node][1] != '.':
        front(tree[node][1],result) 
def mid(node,result):
    
    if tree[node][0] != '.':
        mid(tree[node][0],result)
    result.append(node)   
    if tree[node][1] != '.':
        mid(tree[node][1],result)
def back(node,result):
    if tree[node][0] != '.':
        back(tree[node][0],result)
    if tree[node][1] != '.':
        back(tree[node][1],result)
    result.append(node)   
    

n = int(input())
tree = {}

for q in range(n):
    m, l, r = input().split()
    tree[m] = l,r

result = []
front('A',result)

for q in result:
    print(q, end = '')
print()
result = []

mid('A',result)
for q in result:
    print(q, end = '')
print()
result = []
back('A',result)
for q in result:
    print(q, end = '')


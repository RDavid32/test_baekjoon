import sys
import re 
input = sys.stdin.readline

word = str(input().rstrip("\n"))
pattern = re.compile('(100+1+|01)+') 
result = pattern.fullmatch(word) 

if result:
    print("SUBMARINE")
else:
    print("NOISE")
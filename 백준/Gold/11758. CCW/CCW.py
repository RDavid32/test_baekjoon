
import sys
input = sys.stdin.readline 
arr = [list(map(int,input().split())) for _ in range(3)]

def ccw(id1,id2,id3):
    return (id1[0]*id2[1] + id2[0]*id3[1] + id3[0]*id1[1] - (id2[0]*id1[1] + id3[0]*id2[1] + id1[0]*id3[1]))

answer = ccw(arr[0],arr[1],arr[2])

if answer > 0:
    print(1)
elif answer == 0:
    print(0)
else:
    print(-1)
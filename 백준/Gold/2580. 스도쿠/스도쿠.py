def row(y, n): 
    for q in range(9):
        if n == sudoku[y][q]:
            return False
    return True

def column(x, n):
    for q in range(9):
        if n == sudoku[q][x]:
            return False
    return True

def square(y, x, n):
    for q in range(3):
        for w in range(3):
            if n == sudoku[y//3 * 3 + q][x//3 * 3 + w]: 
                return False
    return True

def find(n):
    if n == len(blank): 
        for i in sudoku: 
            print(*i) 
        exit() 

    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

import sys
input = sys.stdin.readline
sudoku = [list(map(int,input().split())) for _ in range(9)]
blank = []
for q in range(9):
    for w in range(9):
        if sudoku[q][w] == 0:
            blank.append([q,w])
find(0)

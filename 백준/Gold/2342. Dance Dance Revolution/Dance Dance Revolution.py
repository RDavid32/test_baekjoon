def ddr(i ,j ,k ,count):
    if (i,k) in nd:
        if d[(j ,k)] + count < nd[(i ,k)]:
            nd[(i ,k)] = d[(j ,k)] + count
    else:
        nd[(i ,k)] = d[(j ,k)] + count

def ddr2(i ,j ,k ,count):
    if (j ,i) in nd:
        if d[(j ,k)] + count < nd[(j ,i)]:
            nd[(j ,i)] = d[(j ,k)]+count
    else:
        nd[(j ,i)] = d[(j ,k)] + count

arr = list(map(int,input().split()))[:-1]
d = {(0,0): 0}

for i in arr:
    nd = {}
    for j ,k in d:
        if i in (j,k):
            ddr(j ,j ,k ,1)
        else:
            if (i ,j) in [(1,3),(3,1),(2,4),(4,2)]:
                ddr(i ,j ,k ,4)
            elif j==0:
                ddr(i ,j ,k ,2)
            else:
                ddr(i ,j ,k ,3)
            if (i,k) in [(1,3),(3,1),(2,4),(4,2)]:
                ddr2(i ,j ,k ,4)
            elif k==0:
                ddr2(i ,j ,k ,2)
            else:
                ddr2(i ,j ,k ,3)
    d=nd
    
print(min(d.values()))
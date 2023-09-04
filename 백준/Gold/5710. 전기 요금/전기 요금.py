import sys
input = sys.stdin.readline

def wh_to_bill(bill):

    arr = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]
    if bill <= arr[0]:
        return bill // 2
    if bill <= arr[1]:
        return 100 + (bill - arr[0]) // 3
    if bill <= arr[2]:
        return 10000 + (bill - arr[1]) // 5

    return 1000000 + (bill - arr[2]) // 7

def bill_to_who(wh):
    arr = [100, 10000, 1000000]

    if wh < arr[0]:
        return wh * 2
    
    if wh < arr[1]:
        return 200 + (wh- 100) * 3
    
    if wh < arr[2]:
        return 200 + 29700 + (wh - 10000) * 5
    return 200 + 29700 + 4950000  + (wh - 1000000) * 7

def binary_search(start,end, target):
    total_wh = end 

    while True:
        me = (start + end) // 2  
        other = total_wh - me

        check = bill_to_who(other) - bill_to_who(me)

        if check == B:
            return bill_to_who(me)

        if check > B:
            start = me + 1
            
        else:
            end = me - 1
            
while True:
    A, B = map(int,input().split())
    
    if A + B == 0:
        break
    
    total_wh = wh_to_bill(A)    
    print(binary_search(1,total_wh,B))
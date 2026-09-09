def solution(citations):
    citations.sort()
    
    n = len(citations)

    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2
        
        check = n - mid
        
        if citations[mid] >= check:
            right = mid
        else:
            left = mid + 1
    
    return n - left
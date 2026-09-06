from collections import Counter
def solution(nums):
    answer = len(Counter(nums).keys())
    return min(len(nums) // 2, answer)
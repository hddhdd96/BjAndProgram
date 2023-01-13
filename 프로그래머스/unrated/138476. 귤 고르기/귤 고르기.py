from collections import Counter

def solution(k, tangerine):
    count = 0
    
    arr = sorted(Counter(tangerine).items(), reverse = True, key = lambda x : x[1])
    
    for key, value in arr:
        k -= value
        count += 1
        if k <= 0:
            break
    return count
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque()
    q.append([begin, 0])
    
    while q:
        x, count = q.popleft()
        if x == target:
            return count
        
        for i in range(len(words)):
            diff = 0
            word = words[i]
            for j in range(len(word)):
                if x[j] != word[j]:
                    diff += 1
            if diff == 1:
                q.append([word, count + 1])
        
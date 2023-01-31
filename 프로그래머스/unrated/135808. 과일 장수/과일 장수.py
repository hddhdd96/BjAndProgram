def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)):
        if len(score[i*m:i*m+m]) == m:
            answer += min(score[i*m:i*m+m])*m
    t = 1
    return answer
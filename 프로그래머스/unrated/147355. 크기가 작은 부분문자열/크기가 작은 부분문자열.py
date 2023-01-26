def solution(t, p):
    length = len(p)
    p = int(p)
    answer = 0
    for i in range(len(t) - length + 1):
        if int(t[i: i + length]) <= p:
            answer += 1
    return answer
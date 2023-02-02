def solution(clothes):
    cot = {}
    answer = 1
    for i, j in clothes:
        if j not in cot:
            cot[j] = 1
        else:
            cot[j] += 1
    for value in cot.values():
        answer *= (value +1)
    return answer -1
    
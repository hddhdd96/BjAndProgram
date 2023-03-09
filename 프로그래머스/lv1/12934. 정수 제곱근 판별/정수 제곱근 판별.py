def solution(n):
    answer = 0
    k = pow(n, 0.5)
    if int(k) == k:
        return pow(k+1, 2)
    else:
        return -1
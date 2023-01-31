def solution(arr):
    arr.remove(min(arr))
    t=1
    return arr if arr else [-1]
def solution(n):
    x = n**0.5
    if x % 1 == 0:
        return int((x+1)**2)
    else:
        return -1
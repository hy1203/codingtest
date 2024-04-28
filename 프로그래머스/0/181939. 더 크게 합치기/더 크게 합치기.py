def solution(a, b):
    a_first = int(str(a)+str(b))
    b_first = int(str(b)+str(a))
    return max(a_first,b_first)
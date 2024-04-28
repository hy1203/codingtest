def solution(a, b):
    plus = int(str(a)+str(b))
    mult = 2*a*b
    if plus == mult:
        return plus
    elif plus > mult:
        return plus
    else:
        return mult
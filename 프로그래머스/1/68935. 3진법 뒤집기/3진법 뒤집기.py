def solution(n):
    result=''
    while n >= 1:
        result += str(n%3)
        n //= 3
    return int(result,3)
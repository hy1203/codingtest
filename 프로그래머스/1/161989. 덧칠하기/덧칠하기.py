def solution(n, m, section):
    answer,paint = 0, 0

    for i in section:
        if paint <= i:
            paint = i+m
            answer += 1
    return answer
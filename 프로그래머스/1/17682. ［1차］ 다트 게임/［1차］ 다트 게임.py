def solution(dartResult):
    res=[]
    answer = 0
    dartResult = dartResult.replace("10","t")
    for i in dartResult:
        if i.isnumeric():
            answer += int(i)
            continue
        elif i == 't':
            answer += 10
            continue
        elif i == 'S':
            res.append(answer)
        elif i == 'D':
            res.append(answer**2)
        elif i == 'T':
            res.append(answer**3)
        elif i == '*':
            res[-1] *= 2
            if len(res) >= 2:
                res[-2] *= 2
        elif i == '#':
            res[-1] *= -1
        answer = 0
    return sum(res)
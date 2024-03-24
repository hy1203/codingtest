def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        result = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                result += yearning[j]
        answer.append(result)
    return answer
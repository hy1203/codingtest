def solution(strings, n):
    answer = []
    word = []
    strings.sort()
    for i in strings:
        word.append(i[n])
    word.sort()
    for  i in word:
        for j in strings:
            if j[n] == i and j not in answer:
                answer.append(j)
    return answer
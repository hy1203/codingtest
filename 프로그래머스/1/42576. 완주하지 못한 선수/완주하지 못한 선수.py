def solution(participant, completion):
    d = {}
    for i in participant:
        d[i]= d.get(i,0)+1
    for i in completion:
        d[i] -= 1
    result = [k for k, v in d.items() if v>0]
    answer = result[0]
    return answer
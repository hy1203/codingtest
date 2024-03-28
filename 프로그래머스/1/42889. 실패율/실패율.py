def solution(N, stages):
    answer = {}
    stages = sorted(stages)
    allP = len(stages)
    for i in range(1,N+1):
        if allP != 0:
            answer[i] = stages.count(i)/allP
            allP -= stages.count(i)
        else:
            answer[i] = 0
    return sorted(answer, key = lambda x : answer[x], reverse = True)
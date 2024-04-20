def solution(array):
    answer = [0]*(max(array)+1)
    
    for i in array:
        answer[i] += 1
    max_num = 0
    for i in answer:
        if i == max(answer):
            max_num += 1
    if max_num > 1:
        return -1
    else:
        return answer.index(max(answer))
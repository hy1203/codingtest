def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in list(skip):
        alpha = alpha.replace(i,'')
    for i in s:
        answer += alpha[(alpha.find(i)+index)%len(alpha)]
    return answer
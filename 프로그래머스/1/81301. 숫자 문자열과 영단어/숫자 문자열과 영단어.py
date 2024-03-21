def solution(s):
    answer = ""
    tmp=""
    num_eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(s)):
        if s[i].isnumeric():
            answer += s[i]
        else:
            tmp+=s[i]
            if tmp in num_eng:
                answer += str(num_eng.index(tmp))
                tmp=""
    return int(answer)
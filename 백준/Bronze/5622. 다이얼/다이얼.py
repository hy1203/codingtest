d = input()
number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result = 0

for i in d:
    for j in number:
        if i in j:
            result += number.index(j)+3
print(result)

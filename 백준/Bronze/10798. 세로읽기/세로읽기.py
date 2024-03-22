word=[]
for i in range(5):
    i = input()
    word.append(i)
for i in range(15):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i],end='')

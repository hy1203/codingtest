t = int(input())
result = []
for _ in range(t):
    word = input()
    result.append(word)
for w in result:
    print(w[0],w[-1],sep='')

c = [1,1,2,2,2,8]
haveC = list(map(int,input().split()))
for i in range(len(c)):
    if c[i] == haveC[i]:
        c[i] = 0
    else:
        c[i] -= haveC[i]
for i in c:
    print(i, end=' ')

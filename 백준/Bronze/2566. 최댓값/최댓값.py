num = []
for i in range(9):
    i = list(map(int,input().split()))
    num.append(i)
result = max(map(max,num))
print(result)
for i in range(9):
    for j in range(9):
        if num[i][j] == result:
            print(i+1, j+1)
            break
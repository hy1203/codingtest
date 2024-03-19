n, m = map(int,input().split())
result=[]
for i in range(1, n+1):
    result.append(i)
for _ in range(m):
    i,j = map(int,input().split())
    num = result[i-1]
    result[i-1] = result[j-1]
    result[j-1] = num
for i in result:
    print(i, end=' ')
        

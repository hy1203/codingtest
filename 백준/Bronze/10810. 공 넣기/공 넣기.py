n, m = map(int,input().split())
result = [0]*n
for _ in range(m):
    i, j, k = map(int,input().split())
    for t in range(i,j+1):
        result[t-1] = k
for i in result:
    print(i, end=' ')
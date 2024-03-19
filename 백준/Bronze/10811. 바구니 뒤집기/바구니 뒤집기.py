n, m = map(int,input().split())
result = [i for i in range(1,n+1)]
tmp = 0

for _ in range(m):
    i, j = map(int,input().split())
    tmp = result[i-1:j]
    tmp.reverse()
    result[i-1:j] = tmp

for i in result:
    print(i, end=' ')

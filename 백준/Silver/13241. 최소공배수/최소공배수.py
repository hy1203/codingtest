import sys
a,b = map(int,sys.stdin.readline().split())
result = []
for i in range(1, b+1):
    if a%i == 0 and b%i == 0:
        result.append(i)
print(a*b//max(result))

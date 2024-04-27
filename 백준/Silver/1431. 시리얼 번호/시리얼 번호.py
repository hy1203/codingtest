import sys
input = sys.stdin.readline
n = int(input())
result = []

for _ in range(n):
    s = input().rstrip()
    sum1 = 0
    for i in s:
        if i.isdigit():
            sum1 += int(i)
    result.append((s,sum1))

result = sorted(result, key = lambda x :(len(x[0]),x[1],x[0]))

for r in result:
    print(r[0])
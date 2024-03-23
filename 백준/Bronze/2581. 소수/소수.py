n = int(input())
m = int(input())
result = []

for i in range(n, m+1):
    fake = []
    for j in range(1, i+1):
        if i%j == 0:
            fake.append(j)
    if len(fake) == 2:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))

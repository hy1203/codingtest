result = []
for i in range(10):
    i = int(input())
    result.append((i%42))
print(len(set(result)))

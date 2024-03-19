n = [i for i in range(1,31)]
for i in range(1,29):
    i=int(input())
    n.remove(i)
print(min(n))
print(max(n))

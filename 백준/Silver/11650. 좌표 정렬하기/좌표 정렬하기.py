n = int(input())
num = []

for _ in range(n):
    x, y = map(int,input().split())
    num.append([x,y])
for i in sorted(num):
    print(i[0], i[1])

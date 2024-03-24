import sys
n = int(input())
num = list(map(int,sys.stdin.readline().split()))

new_num = sorted(set(num))

dic = {new_num[i]:i for i in range(len(new_num))}

for i in num:
    print(dic[i], end=' ')

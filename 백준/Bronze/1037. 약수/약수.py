n = input()
real = list(map(int,input().split()))
real = sorted(real)
print(real[0]*real[-1])

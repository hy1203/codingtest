a,b = map(int,input().split())
a = str(a)[::-1]
b = str(b)[::-1]
if a < b:
    print(int(b))
else:
    print(int(a))

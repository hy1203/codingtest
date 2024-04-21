a,b = map(int, input().split())
a1 = list(map(int,input().split()))
b1 = list(map(int,input().split()))

a_com = set(a1)-set(b1)
b_com = set(b1)-set(a1)

print(len(a_com)+len(b_com))
m = int(input())
cup = [1,2,3]
for _ in range(m):
    x, y = map(int,input().split())
    movex = cup.index(x)
    movey = cup.index(y)
    cup[movex],cup[movey] = y, x
    
print(cup[0])
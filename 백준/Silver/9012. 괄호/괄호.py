n = int(input())
for _ in range(n):
    ps = input()
    vps = []
    for i in ps:
        if i == '(':
            vps.append(i)
        elif i == ')':
            if vps:
                vps.pop()
            else:
                print('NO')
                break
    else:
        if not vps:
            print('YES')
        else:
            print('NO')
import sys
n = int(input())
stack=[]

for i in range(n):
    i = sys.stdin.readline().rstrip()
    if len(i)>2:
        stack.append(int(i[2:]))
    elif i == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif i == '3':
        print(len(stack))
    elif i == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

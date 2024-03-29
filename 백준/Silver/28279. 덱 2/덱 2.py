import sys
from collections import deque

n = int(input())
dequeue = deque()

for i in range(n):
    i = sys.stdin.readline().split()
    if i[0] == '1':
        dequeue.appendleft(i[1])
    elif i[0] == '2':
        dequeue.append(i[1])
    elif i[0] == '3':
        if dequeue:
            print(dequeue.popleft())
        else:
            print(-1)
    elif i[0] == '4':
        if dequeue:
            print(dequeue.pop())
        else:
            print(-1)
    elif i[0] == '5':
        print(len(dequeue))
    elif i[0] == '6':
        if dequeue:
            print(0)
        else:
            print(1)
    elif i[0] == '7':
        if dequeue:
            print(dequeue[0])
        else:
            print(-1)
    else:
        if dequeue:
            print(dequeue[-1])
        else:
            print(-1)

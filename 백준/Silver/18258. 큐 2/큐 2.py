import sys
from collections import deque
n = int(input())
queue = deque()
for i in range(n):
    i = sys.stdin.readline().split()
    if i[0] == 'push':
        queue.append(int(i[1]))
    elif i[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    else:
        if not queue:
            print(-1)
        else:
            print(queue[-1])
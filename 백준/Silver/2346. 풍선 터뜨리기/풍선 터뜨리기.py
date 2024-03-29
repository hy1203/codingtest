import sys
from collections import deque
n = int(input())

deque = deque(enumerate(map(int,sys.stdin.readline().split()), start = 1))

while deque:
    idx = deque.popleft()
    print(idx[0], end=' ')
    if idx[1] > 0:
        deque.rotate(-(idx[1]-1))
    else:
        deque.rotate(-idx[1])

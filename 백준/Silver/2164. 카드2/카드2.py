from collections import deque
n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
while len(queue) != 1:
    queue.popleft()
    moveNum = queue.popleft()
    queue.append(moveNum)
print(queue[0])
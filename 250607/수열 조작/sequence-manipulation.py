n = int(input())

# Please write your code here.
from collections import deque


dq =deque()
for i in range(1, n+1):
    dq.append(i)

while len(dq) != 1:
    dq.popleft()
    if dq:
        dq.append(dq.popleft())

print(dq[0])
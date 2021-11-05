import sys
from collections import deque
sys.stdin = open('input.txt')
N = int(sys.stdin.readline().rstrip())
q = deque([[N, []]])
total = [N]*1000000
while q:
    a, b = q.popleft()
    if len(b)> len(total):
        continue
    if a == 0:
        if len(total) > len(b):
            total = b[:-1]
            break
    else:
        if a%3 == 0:
            q.append([a//3, b+[a//3]])
        if a%2 == 0:
            q.append([a//2, b+[a//2]])
        q.append([a-1, b+[a-1]])
print(len(total))
print(N, end=' ')
for to in total:
    print(to, end=" ")


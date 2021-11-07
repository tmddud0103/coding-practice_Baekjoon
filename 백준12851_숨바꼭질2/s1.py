import sys
sys.stdin = open('input.txt')
from collections import deque

maxnum = 100001
stack = [0] * (maxnum+1)
N, K = list(map(int, input().split()))
q = deque()
q.append([N, 0])
cnt = 0
total = 100001
while len(q) >0:
    # print(q)
    x, y = q.popleft()
    if x == K:
        # print(stack[x])
        total = stack[x]
        cnt +=1
        ans = y
        continue
    if total < y:
        break
    for a in (x-1, x+1, x*2):
        if 0 <= a <= maxnum and (stack[a] == 0 or stack[a] == stack[x] + 1):
            stack[a] = stack[x] + 1
            q.append([a, y+1])
print(ans)
print(cnt)
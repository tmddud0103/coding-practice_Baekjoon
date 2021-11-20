import sys
sys.stdin = open('input.txt')
from collections import deque

maxnum = 100001
stack = [0] * (maxnum+1)
dist = [-1] * (maxnum+1)
N, K = list(map(int, input().split()))
q = deque()
q.append(N)
stack[N] = 9
dist[N] = 0

while q:
    now = q.popleft()
    if now*2 <= maxnum and stack[now*2] == 0:  # 순간이동
        q.appendleft(now*2)
        stack[now*2] = 9
        dist[now*2] = dist[now]
    if now + 1 <= maxnum and stack[now+1] == 0: # x+1이동
        q.append(now+1)
        stack[now+1] = 9
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and stack[now-1] == 0: # x-1이동
        q.append(now-1)
        stack[now-1] = 9
        dist[now-1] = dist[now] + 1
print(dist[K])
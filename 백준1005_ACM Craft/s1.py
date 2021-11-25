import sys
from collections import deque
sys.stdin = open('input.txt')
TC = int(sys.stdin.readline().lstrip())

for tc in range(TC):
    n, k = map(int, sys.stdin.readline().split())
    nlist = [0] + list(map(int, sys.stdin.readline().split()))
    tree = [[] for _ in range(n+1)]
    cost = [0] * (n+1)
    not_complete = [0] *(n+1)
    for _ in range(k):
        a, b =  list(map(int, sys.stdin.readline().split()))
        not_complete[b] += 1
        tree[a].append(b)

    q = deque()
    for i in range(1, n+1):
        if not_complete[i] == 0:
            q.append(i)
            cost[i] = nlist[i]
    while q:
        now = q.popleft()
        for i in tree[now]:

            not_complete[i] -= 1
            cost[i] = max(nlist[i] + cost[now], cost[i])
            if not_complete[i] == 0:
                q.append(i)
    win = int(sys.stdin.readline())
    print(cost[win])
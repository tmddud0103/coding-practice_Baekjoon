import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().lstrip())
check = [0] *(n+1)
check[1] = 1
child = [[0] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    child[a].append(b)
    child[b].append(a)
q = deque([1])
while q:
    i = q.popleft()
    for j in range(1, len(child[i])):
        if check[child[i][j]] != 0:
            pass
        else:
            check[child[i][j]] = i
            q.append(child[i][j])

for i in range(2, n+1):
    print(check[i])
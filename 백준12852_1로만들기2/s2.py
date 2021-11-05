import sys
from collections import deque
sys.stdin = open('input.txt')
N = int(sys.stdin.readline().rstrip())
nlist = [[10000000,0]for _ in range(N+1)]
nlist[1] = [0,0]
q = deque([1])
while q:
    a = q.popleft()
    if a == N:
        break
    if a*3 <= N and nlist[a*3][0] > nlist[a][0]+1:
        nlist[a*3] = [nlist[a][0]+1, a]
        q.append(a*3)
    if a*2<=N and nlist[a*2][0] > nlist[a][0]+1:
        nlist[a * 2] = [nlist[a][0] + 1, a]
        q.append(a*2)
    if nlist[a+1][0] > nlist[a][0]+1:
        nlist[a+1] = [nlist[a][0]+1,a]
        q.append(a +1)
print(nlist[N][0])
a = N
while a != 0:
    print(a, end = ' ')
    a = nlist[a][1]
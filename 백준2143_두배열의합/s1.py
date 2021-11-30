import sys
from collections import defaultdict
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

dictA = defaultdict(int)


ans = 0

for i in range(N):
    for j in range(i, N):
        dictA[sum(A[i:j+1])] += 1

for i in range(M):
    for j in range(i, M):
        ans += dictA[T - sum(B[i:j+1])]

print(ans)
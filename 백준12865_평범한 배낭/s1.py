# 실패
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
nlist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_total = 0

def bag(k, i, total):
    global max_total
    for j in range(i, N):
        if nlist[j][0]<=k:
            bag(k-nlist[j][0], j+1, total + nlist[j][1])
    if max_total< total:
        max_total = total
bag(K, 0, 0)
print(max_total)
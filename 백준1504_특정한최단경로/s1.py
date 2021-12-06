import heapq
import sys
sys.stdin = open('input.txt')


n, e = map(int, sys.stdin.readline().split())
mat = [[] for i in range(n + 1)]
inf = 100000000

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    mat[a].append([b, c])
    mat[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    dp = [inf for _ in range(n + 1)]
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])
    while heap:
        w, c = heapq.heappop(heap)
        for n_n, n_w in mat[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heapq.heappush(heap, [wei, n_n])
    return dp
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < inf else -1)
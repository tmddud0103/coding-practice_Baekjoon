import sys
import heapq
sys.stdin = open('input.txt')
INF = 100000000
N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
least_bus = [INF]*(N+1)
bus = []
cnt_bus = [0]*(N+1)
for _ in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    cnt_bus[temp[0]] += 1
    bus.append(temp)
bus.sort()
start, end = map(int, sys.stdin.readline().split())
least_bus[start] = 0
least_bus[0] = 0
for i in range(1, N+1):
    cnt_bus[i] += cnt_bus[i-1]
q = [[0, 0, start]]
while q:
    c, s, e = heapq.heappop(q)
    for i in range(cnt_bus[e-1], cnt_bus[e]):
        new=least_bus[bus[i][0]] + bus[i][2]
        if new < least_bus[bus[i][1]]:
            least_bus[bus[i][1]] = new
            heapq.heappush(q, [least_bus[bus[i][1]], e, bus[i][1]])
print(least_bus[end])
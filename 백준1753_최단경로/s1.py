import sys
import heapq
sys.stdin = open('input.txt')


n, e = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline().rstrip())
distance = [10000000] * (n+1)
distance[start] = 0
graph = {}

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    if u in graph:
        if v in graph[u]:
            graph[u][v] = min(graph[u][v], w)
        else:
            graph[u][v] = w
    else:
        graph[u] = {v: w}

q=[(0, start)]
while q:
    current_distance, current_destination = heapq.heappop(q)
    if distance[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
        continue
    if current_destination in graph:
        for new_destination, new_distance in graph[current_destination].items():
            temp = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if temp < distance[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distance[new_destination] = temp
                heapq.heappush(q, [temp, new_destination])
for i in range(1, n+1):
    if distance[i] == 10000000:
        print('INF')
    else:
        print(distance[i])

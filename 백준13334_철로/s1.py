import sys
import heapq
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
road_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = int(sys.stdin.readline())

roads = []
for road in road_list:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
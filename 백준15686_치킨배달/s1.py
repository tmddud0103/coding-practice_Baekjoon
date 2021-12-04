import sys
from itertools import combinations

sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
mat = []
houses = []
chicken_shop = []
for i in range(n):
    temp = []
    for j, x in enumerate(sys.stdin.readline().split()):
        if int(x) == 1:
            houses.append((i, j))
        elif int(x) == 2:
            chicken_shop.append((i, j))
        temp.append(int(x))
    mat.append(temp)

result = []

for picked_shops in list(combinations(chicken_shop, m)):
    city_chicken_dist = 0
    for hy, hx in houses:
        dists = []
        for sy, sx in picked_shops:
            dist = abs(hy-sy) + abs(hx-sx)
            dists.append(dist)
        city_chicken_dist += min(dists)
    result.append(city_chicken_dist)

print(min(result))

import sys
import heapq
sys.stdin = open('input.txt')

TC = int(sys.stdin.readline().rstrip())
for tc in range(TC):
    m, n = map(int, sys.stdin.readline().split())
    check = [0]*m
    que = []
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        if x <= y:
            heapq.heappush(que,[x, y])
            heapq.heappush(que, [x+m, y+m])
        else:
            heapq.heappush(que,[x, y+m])
    temp = 0
    if m < n:
        print('NO')
    else:
        while que:
            x, y = heapq.heappop(que)

            while temp < x:
                temp += 1
            if temp > y:
                print('NO')
                heapq.heappush(que, [x, y])
                break
            else:
                if check[temp%n] == 1:
                    while check[temp%n] == 1:
                        temp += 1
                    if temp > y:
                        print('NO')
                        heapq.heappush(que, [x, y])
                        break
                check[temp%n] = 1
                temp += 1

        if len(que) == 0:
            print('YES')
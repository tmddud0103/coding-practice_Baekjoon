import sys
sys.stdin = open('input.txt')

TC = int(sys.stdin.readline().rstrip())

for _ in range(TC):
    n = int(sys.stdin.readline().rstrip())
    l1 = list(map(int, sys.stdin.readline().split()))
    l2 = list(map(int, sys.stdin.readline().split()))
    if n > 1:
        l1[1] += l2[0]
        l2[1] += l1[0]
    if n > 2:
        for i in range(2, n):
            l1[i] += max(l1[i-2], l2[i-1], l2[i-2])
            l2[i] += max(l2[i - 2], l1[i - 1], l1[i-2])
    print(max(l1[-1], l2[-1]))

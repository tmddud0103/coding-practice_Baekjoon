import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())
nlist = list(map(int, sys.stdin.readline().split()))
ans = []
total = 2000000001
a = 0
b = n-1
while a < b:
    # print(a, b)
    temp = nlist[b] + nlist[a]
    abstemp = abs(temp)
    if total > abstemp:
        total = abstemp
        ans = [nlist[a], nlist[b]]
    if temp > 0:
        b -= 1
    elif temp < 0:
        a += 1
    else:
        break
print(ans[0], ans[1])
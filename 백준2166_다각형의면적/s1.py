import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())
nlist = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nlist.append(nlist[0])

# print(nlist)
total = 0
for i in range(n):
    total += nlist[i][0] * nlist[i+1][1] - nlist[i][1] * nlist[i+1][0]
print(abs(total) * (1/2))
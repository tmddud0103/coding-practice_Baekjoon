import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline().lstrip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    mat[i][0] += min(mat[i-1][1],mat[i-1][2])
    mat[i][1] += min(mat[i-1][0],mat[i-1][2])
    mat[i][2] += min(mat[i-1][1],mat[i-1][0])

print(min(mat[-1]))
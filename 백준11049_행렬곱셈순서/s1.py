import sys
sys.stdin = open('input.txt')


n = int(sys.stdin.readline())
rc = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
mat = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        x = j + i
        # mat[j][x] = 2 ** 32
        for k in range(j, x):
            # mat[j][x] = min(mat[j][x], mat[j][k] + mat[k + 1][x] + rc[j][0] * rc[k][1] * rc[x][1])
            mat[j][x] = mat[j][k] + mat[k + 1][x] + rc[j][0] * rc[k][1] * rc[x][1]
print(mat[0][n - 1])
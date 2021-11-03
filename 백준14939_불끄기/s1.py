import sys
sys.stdin = open('input.txt')


mat = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(10)]
dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
total = 101
def asd(r, c):
    global a
    for i in range(5):
        x = r + dx[i]
        y = c + dy[i]
        if 0<=x<10 and 0<=y<10:
            if a[x][y] == '#':
                a[x][y] = 'O'
            else: a[x][y] = '#'

for k in range(1<<10):
    cnt = 0
    a = []
    for i in range(10):
        a.append(mat[i][:])

    for i in range(10):
        if k & (1<<i):
            cnt += 1
            asd(0, i)
    for i in range(1, 10):
        for j in range(10):
            if a[i-1][j] == 'O':
                asd(i, j)
                cnt += 1

    for i in range(10):
        if a[9][i] == 'O':
            cnt = 101
    total = min(total, cnt)

print(total if total != 101 else -1)
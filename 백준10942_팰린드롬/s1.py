import sys
sys.stdin = open('input.txt')


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

mat = [[0] * n for _ in range(n)]

for i in range(n):
    for start in range(n - i):
        end = start + i
        if start == end:
            mat[start][end] = 1
        elif numbers[start] == numbers[end]:
            if start + 1 == end:
                mat[start][end] = 1
            elif mat[start + 1][end - 1] == 1:
                mat[start][end] = 1
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(mat[s - 1][e - 1])

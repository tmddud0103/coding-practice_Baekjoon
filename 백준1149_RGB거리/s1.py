# 시간 초과나서 다른 방법으로 품
import sys
sys.stdin = open('input.txt')

def dfs(row, temp, no):
    global mat, n, total
    if temp > total:
        return
    if row == n:
        if temp < total:
            total = temp
        return
    for i in range(3):
        if i != no:
            dfs(row+1, temp + mat[row][i], i)

n = int(sys.stdin.readline().lstrip())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
total = 1000*n
dfs(0, 0, -1)
print(total)


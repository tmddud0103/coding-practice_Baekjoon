import sys
sys.stdin = open('input.txt')
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
passed = [0]* 26

def dfs(x, y, ans):
    global answer
    if ans > answer:
        answer = ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < R) and (0 <= ny < C) and (passed[board[nx][ny]]==0):
            passed[board[nx][ny]]=1
            dfs(nx, ny, ans+1)
            passed[board[nx][ny]]=0

R, C = map(int, sys.stdin.readline().split())
board = [list(map(lambda a : ord(a)-65,sys.stdin.readline().strip())) for _ in range(R)]
passed[board[0][0]]=1
answer = 1
dfs(0, 0, answer)
print(answer)
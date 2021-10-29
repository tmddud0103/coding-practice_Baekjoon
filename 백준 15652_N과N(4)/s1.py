import sys
sys.stdin = open('input.txt')


n, m = map(int, sys.stdin.readline().split())

def dfs(now, cnt):
    global m, total, n, temp
    if cnt == m:
        total.append(temp[:])
        return
    for j in range(now, n+1):
        temp.append(j)
        dfs(j, cnt+1)
        temp.pop()


total = []
temp = []
for i in range(1, n+1):
    temp.append(i)
    dfs(i, 1)
    temp.pop()
for i in range(len(total)):
    for j in range(m):
        print(total[i][j],end=' ')
    print()
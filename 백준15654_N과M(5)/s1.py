import sys
sys.stdin = open('input.txt')

def dfs(k):
    global n, m, nlist, total, temp
    if k == m:
        total.append(temp[:])
        return
    for i in range(n):
        if check[i]==0:
            check[i]=1
            temp.append(nlist[i])
            dfs(k+1)
            check[i]=0
            temp.pop()



n, m = map(int, sys.stdin.readline().split())
nlist = sorted(list(map(int, sys.stdin.readline().split())))
total = []
temp = []
check = [0]*(n+1)
dfs(0)
for i in range(len(total)):
    for j in range(m):
        print(total[i][j], end=' ')
    print()